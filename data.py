import pandas as pd
import numpy as np
from datetime import datetime

# 定义生成的数据条数
num_rows = 300

# 创建时间序列
start_date = datetime(2020, 1, 4, 0, 0, 0)
hours = pd.date_range(start_date, periods=num_rows, freq="h")

# 创建温度和pH序列
temperature = np.tile(
    [
        20,
        19,
        18,
        17,
        16.5,
        16,
        16,
        16.5,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        23.5,
        23.5,
        23,
        22.5,
        22,
        21.5,
        21,
        20.5,
        20,
    ],
    num_rows // 24 + 1,
)[:num_rows]
ph = np.tile(
    [
        7,
        6.9,
        6.8,
        6.7,
        6.7,
        6.8,
        6.9,
        7,
        7.1,
        7.3,
        7.4,
        7.5,
        7.6,
        7.8,
        7.9,
        7.9,
        7.8,
        7.7,
        7.5,
        7.3,
        7.1,
        7,
        7,
        7,
    ],
    num_rows // 24 + 1,
)[:num_rows]

# 添加随机噪声
temperature_noise = np.random.normal(0, 0.2, num_rows)
ph_noise = np.random.normal(0, 0.05, num_rows)

temperature += temperature_noise
ph += ph_noise

# 创建DataFrame
df = pd.DataFrame({"date": hours, "temperature": temperature, "ph": ph})

# 写入到CSV文件
df.to_csv("water_quality.csv", index=False)
