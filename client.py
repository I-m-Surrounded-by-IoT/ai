import predict_pb2, predict_pb2_grpc
import grpc
import pandas as pd
import utils

with grpc.insecure_channel("localhost:50051") as channel:
    stub = predict_pb2_grpc.WaterQualityServiceStub(channel)
    df = pd.read_csv("water_quality.csv")

    request = predict_pb2.PredictReq(
        qualities=utils.df2data(df), look_back=3, horizon=24
    )
    response = stub.Predict(request)
    print(response)
