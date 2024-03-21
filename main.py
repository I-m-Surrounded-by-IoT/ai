import predict_pb2_grpc
import predict_pb2
import grpc
import pandas as pd
import guess
from concurrent import futures
import utils


class Predictor(predict_pb2_grpc.WaterQualityServiceServicer):
    def __init__(self, model_path, scaler_path):
        self.predictor = guess.Predictor(model_path, scaler_path)

    def Predict(self, request, context):
        df = utils.data2df(request.qualities)
        look_back = request.look_back
        horizon = request.horizon
        predictions = self.predictor.predict(df, look_back, horizon)
        return predict_pb2.PredictResp(qualities=utils.df2data(predictions))


if __name__ == "__main__":
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    predict_pb2_grpc.add_WaterQualityServiceServicer_to_server(
        Predictor("model.keras", "scaler.pkl"), server
    )
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()
