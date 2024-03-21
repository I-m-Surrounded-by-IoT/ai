import predict_pb2
import pandas as pd
import numpy as np


def df2data(data):
    qualities = []
    for _, row in data.iterrows():
        quality = predict_pb2.Quality(
            timestamp=int(pd.to_datetime(row["date"]).timestamp()),
            temperature=row["temperature"],
            ph=row["ph"],
        )
        qualities.append(quality)
    return qualities


def data2df(data):
    arr = []
    for quality in data:
        arr.append(
            {
                "date": pd.to_datetime(quality.timestamp, unit="s"),
                "temperature": quality.temperature,
                "ph": quality.ph,
            }
        )
    df = pd.DataFrame(
        arr,
        columns=["date", "temperature", "ph"],
    )
    return df
