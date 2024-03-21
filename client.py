import predict_pb2, predict_pb2_grpc
import grpc
import pandas as pd
import utils
from random import randint

with grpc.insecure_channel("localhost:50051") as channel:
    stub = predict_pb2_grpc.WaterQualityServiceStub(channel)
    df = pd.read_csv("water_quality.csv")

    request = predict_pb2.PredictReq(
        qualities=utils.df2qualitys(df), look_back=3, horizon=24
    )
    response = stub.Predict(request)
    print(response)

    randQuality = df.iloc[randint(0, len(df))]
    request = utils.df2quality(randQuality)
    response = stub.GuessLevel(request)
    print(response.level)
