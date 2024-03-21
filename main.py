import predict_pb2_grpc
import predict_pb2
import grpc
import predict.guess as predict_guess
import level.guess as level_guess
from concurrent import futures
import utils


class Predictor(predict_pb2_grpc.WaterQualityServiceServicer):
    def __init__(self, model_path, scaler_path, level_model_path):
        self.predictor = predict_guess.Predictor(model_path, scaler_path)
        self.level_guesser = level_guess.Predictor(level_model_path)

    def Predict(self, request, context):
        df = utils.qualitys2df(request.qualities, withDate=True)
        look_back = request.look_back
        horizon = request.horizon
        predictions = self.predictor.predict(df, look_back, horizon)
        return predict_pb2.PredictResp(qualities=utils.df2qualitys(predictions))

    def GuessLevel(self, request, context):
        df = utils.quality2df(request)
        prediction = self.level_guesser.predict(df)
        return predict_pb2.GuessLevelResp(level=prediction)


if __name__ == "__main__":
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    predict_pb2_grpc.add_WaterQualityServiceServicer_to_server(
        Predictor("model.keras", "scaler.pkl", "water_quality_level.joblib"), server
    )
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()
