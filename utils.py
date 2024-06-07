import waterquality_pb2
import pandas as pd


def df2quality(data):
    return waterquality_pb2.Quality(
        timestamp=int(pd.to_datetime(data["date"]).timestamp() * 1000),
        temperature=data["temperature"],
        ph=data["ph"],
        tsw=data["tsw"],
        tds=data["tds"],
        oxygen=data["oxygen"],
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
        "tsw": quality.tsw,
        "tds": quality.tds,
        "oxygen": quality.oxygen,
    }
    if withDate:
        obj["date"] = pd.to_datetime(quality.timestamp, unit="ms")
    return obj


def quality2df(quality, withDate=False):
    columns = ["temperature", "ph", "tsw", "tds", "oxygen"]
    if withDate:
        columns = ["date", "temperature", "ph", "tsw", "tds", "oxygen"]
    df = pd.DataFrame(
        [quality2obj(quality, withDate=withDate)],
        columns=columns,
    )
    return df


def qualitys2df(data, withDate=False):
    arr = []
    columns = ["temperature", "ph", "tsw", "tds", "oxygen"]
    if withDate:
        columns = ["date", "temperature", "ph", "tsw", "tds", "oxygen"]
    for quality in data:
        arr.append(quality2obj(quality, withDate=withDate))
    df = pd.DataFrame(
        arr,
        columns=columns,
    )
    return df
