import pandas as pd
import numpy as np
import joblib


def check_columns(data):
    with open("expected_level_columns.txt", "r") as f:
        expected_columns = [line.strip() for line in f]
    if not np.array_equal(data.columns, expected_columns):
        data = data[expected_columns]
    return data


class Predictor:
    def __init__(self, model_path):
        self.model = joblib.load(model_path)

    def predict(self, data):
        data = check_columns(data)
        prediction = self.model.predict(data)
        return prediction[0]


if __name__ == "__main__":
    new_data = pd.DataFrame(
        [
            {
                "temperature": 20.515587888514176,
                "ph": 10.976586304305082,
            }
        ],
    )
    predictor = Predictor("water_quality_level.joblib")
    prediction = predictor.predict(new_data)
    print(f"预测的污染等级为：{prediction}")
