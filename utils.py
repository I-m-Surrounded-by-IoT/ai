import waterquality_pb2
import pandas as pd
import numpy as np


def df2quality(data):
    return waterquality_pb2.Quality(
        timestamp=int(pd.to_datetime(data["date"]).timestamp()),
        temperature=data["temperature"],
        ph=data["ph"],
    )


def df2qualitys(data):
    qualities = []
    for _, row in data.iterrows():
        qualities.append(df2quality(row))
    return qualities


def quality2obj(quality, withDate=False):
    obj = {
        "temperature": quality.temperature,
        "ph": quality.ph,
    }
    if withDate:
        obj["date"] = pd.to_datetime(quality.timestamp, unit="s")
    return obj


def quality2df(quality, withDate=False):
    columns = ["temperature", "ph"]
    if withDate:
        columns = ["date", "temperature", "ph"]
    df = pd.DataFrame(
        [quality2obj(quality, withDate=withDate)],
        columns=columns,
    )
    return df


def qualitys2df(data, withDate=False):
    arr = []
    columns = ["temperature", "ph"]
    if withDate:
        columns = ["date", "temperature", "ph"]
    for quality in data:
        arr.append(quality2obj(quality, withDate=withDate))
    df = pd.DataFrame(
        arr,
        columns=columns,
    )
    return df
