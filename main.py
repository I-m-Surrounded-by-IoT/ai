import json
from os import environ
import uuid
import waterquality_pb2_grpc
import waterquality_pb2
import grpc
import predict.guess as predict_guess
import level.guess as level_guess
from concurrent import futures
import utils
import etcd3
import time
from dataclasses import dataclass
from typing import List, Dict
from dataclasses import asdict


class Predictor(waterquality_pb2_grpc.WaterQualityServiceServicer):
    def __init__(self, model_path, scaler_path, level_model_path):
        self.predictor = predict_guess.Predictor(model_path, scaler_path)
        self.level_guesser = level_guess.Predictor(level_model_path)

    def Predict(self, request, context):
        df = utils.qualitys2df(request.qualities, withDate=True)
        look_back = request.look_back
        horizon = request.horizon
        predictions = self.predictor.predict(df, look_back, horizon)
        return waterquality_pb2.PredictResp(qualities=utils.df2qualitys(predictions))

    def GuessLevel(self, request, context):
        df = utils.quality2df(request)
        prediction = self.level_guesser.predict(df)
        return waterquality_pb2.GuessLevelResp(level=prediction)


@dataclass
class ServiceInstance:
    id: str
    name: str
    version: str
    metadata: Dict[str, str]
    endpoints: List[str]

    def __init__(self, id, name, version, metadata, endpoints):
        self.id = id
        self.name = name
        self.version = version
        self.metadata = metadata
        self.endpoints = endpoints

    def __str__(self):
        return json.dumps(asdict(self))


def keepalive(lease):
    while True:
        lease.refresh()
        time.sleep(5)


def init_config():
    host = environ.get("HOST", "127.0.0.1")
    port = environ.get("PORT", 19000)
    custom_endpoint = environ.get("GRPC_CUSTOM_ENDPOINT")
    if not custom_endpoint:
        custom_endpoint = f"grpc://{host}:{port}"

    etcd_endpoint = environ.get("ETCD_ENDPOINT", "localhost:2379")
    etcd_host = etcd_endpoint.split(":")[0]
    etcd_port = etcd_endpoint.split(":")[1]
    return {
        "host": host,
        "port": port,
        "custom_endpoint": custom_endpoint,
        "etcd_endpoint": etcd_endpoint,
        "etcd_host": etcd_host,
        "etcd_port": etcd_port,
    }


if __name__ == "__main__":
    config = init_config()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    waterquality_pb2_grpc.add_WaterQualityServiceServicer_to_server(
        Predictor("model.keras", "scaler.pkl", "water_quality_level.joblib"), server
    )
    server.add_insecure_port(f"{config['host']}:{config['port']}")
    server.start()

    instance = ServiceInstance(
        id=uuid.uuid4().hex,
        name="water-quality",
        version="1.0.0",
        metadata={},
        endpoints=[config["custom_endpoint"]],
    )
    cli = etcd3.client(
        host=config["etcd_host"],
        port=config["etcd_port"],
    )
    lease = cli.lease(10)
    cli.put(
        f"/microservices/{instance.name}/{instance.id}",
        str(instance),
        lease,
    )
    with futures.ThreadPoolExecutor(max_workers=1) as executor:
        executor.submit(keepalive, lease)

    print(f"Server started at {config['custom_endpoint']}")
    server.wait_for_termination()
