import pandas as pd
import numpy as np
from keras.models import load_model
from datetime import timedelta
import joblib


class Predictor:
    def __init__(self, model_path, scaler_path):
        self.model = load_model(model_path)
        self.scaler = joblib.load(scaler_path)

    def predict(self, data, look_back=3, horizon=24):
        data["date"] = pd.to_datetime(data["date"])
        data = data.set_index("date")
        scaled_data = self.scaler.transform(data)
        X_new = create_dataset(scaled_data, look_back)
        num_features = data.shape[1]
        predictions = predict_sequence(
            self.model, X_new[-1], horizon, num_features, look_back=look_back
        )
        predictions = self.scaler.inverse_transform(predictions)
        time_interval = timedelta(hours=1)
        # 获取新数据集中最后一个观察的时间
        last_date = data.index[-1]
        # 创建一个时间索引
        date_index = pd.date_range(
            start=last_date + time_interval, periods=horizon, freq="h"
        )
        # 创建一个 DataFrame 来保存预测结果
        df = pd.DataFrame(predictions, columns=data.columns)
        df["date"] = date_index
        return check_columns(df)


# 创建用于预测的数据集
def create_dataset(dataset, look_back=1):
    X = []
    for i in range(len(dataset) - look_back):
        a = dataset[i : (i + look_back), :]
        X.append(a)
    return np.array(X)


# 这个函数将使用你的模型和一些初始数据进行预测
def predict_sequence(model, init_seq, horizon, num_features, look_back=3):
    seq = init_seq.copy()
    predictions = []

    for _ in range(horizon):
        # 使用当前序列进行预测
        prediction = model.predict(seq.reshape(1, look_back, num_features))

        # 将预测结果的第一个时间步长添加到预测列表中
        predictions.append(prediction[0][:num_features])

        # 将预测结果的第一个时间步长添加到序列中
        seq = np.vstack((seq[1:], prediction[0][:num_features].reshape(1, -1)))

    return np.array(predictions)


def check_columns(data):
    with open("expected_columns.txt", "r") as f:
        expected_columns = [line.strip() for line in f]
    if not np.array_equal(data.columns, expected_columns):
        data = data[expected_columns]
    return data


if __name__ == "__main__":
    # 加载数据
    data = pd.read_csv("newdata.csv")

    # print(data)

    predictor = Predictor("model.keras", "scaler.pkl")

    look_back = 3
    forecast_horizon = 24

    df = predictor.predict(data, look_back, forecast_horizon)

    print(df)

    # 将 DataFrame 保存为 CSV 文件
    # df.to_csv("predictions.csv")
