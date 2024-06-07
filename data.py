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
        20, 19, 18, 17, 16.5, 16, 16, 16.5, 17, 18, 19, 20,
        21, 22, 23, 23.5, 23.5, 23, 22.5, 22, 21.5, 21, 20.5, 20
    ],
    num_rows // 24 + 1,
)[:num_rows]
ph = np.tile(
    [
        7, 6.9, 6.8, 6.7, 6.7, 6.8, 6.9, 7, 7.1, 7.3, 7.4, 7.5,
        7.6, 7.8, 7.9, 7.9, 7.8, 7.7, 7.5, 7.3, 7.1, 7, 7, 7
    ],
    num_rows // 24 + 1,
)[:num_rows]

# 创建tsw, tds, oxygen序列
tsw = np.tile(
    [
        25, 24.8, 24.6, 24.5, 24.4, 24.3, 24.2, 24.1, 24, 23.9, 23.8, 23.7,
        23.6, 23.5, 23.4, 23.3, 23.2, 23.1, 23, 22.9, 22.8, 22.7, 22.6, 22.5
    ],
    num_rows // 24 + 1,
)[:num_rows]
tds = np.tile(
    [
        500, 495, 490, 485, 480, 475, 470, 465, 460, 455, 450, 445,
        440, 435, 430, 425, 420, 415, 410, 405, 400, 395, 390, 385
    ],
    num_rows // 24 + 1,
)[:num_rows].astype('float64')
oxygen = np.tile(
    [
        8, 7.9, 7.8, 7.7, 7.6, 7.5, 7.4, 7.3, 7.2, 7.1, 7, 6.9,
        6.8, 6.7, 6.6, 6.5, 6.4, 6.3, 6.2, 6.1, 6, 5.9, 5.8, 5.7
    ],
    num_rows // 24 + 1,
)[:num_rows]

# 添加随机噪声
temperature_noise = np.random.normal(0, 0.2, num_rows)
ph_noise = np.random.normal(0, 0.05, num_rows)
tsw_noise = np.random.normal(0, 0.1, num_rows)
tds_noise = np.random.normal(0, 2, num_rows)
oxygen_noise = np.random.normal(0, 0.05, num_rows)

temperature += temperature_noise
ph += ph_noise
tsw += tsw_noise
tds += tds_noise
oxygen += oxygen_noise

# 创建DataFrame
df = pd.DataFrame({
    "date": hours,
    "temperature": temperature,
    "ph": ph,
    "tsw": tsw,
    "tds": tds,
    "oxygen": oxygen
})

# 定义计算污染等级的函数
def calculate_pollution_level(row):
    pollution_score = 0
    if row["temperature"] > 25 or row["temperature"] < 15:
        pollution_score += 1
    if row["ph"] > 7.5 or row["ph"] < 6.5:
        pollution_score += 1
    if row["ph"] > 8 or row["ph"] < 6:
        pollution_score += 1
    if row["tsw"] > 28 or row["tsw"] < 22:
        pollution_score += 1
    if row["tds"] > 600 or row["tds"] < 300:
        pollution_score += 1
    if row["oxygen"] < 6:
        pollution_score += 1
    if row["oxygen"] < 5.5:
        pollution_score += 1

    # 根据污染分数确定污染等级
    if pollution_score >= 6:
        return 5
    elif pollution_score >= 4:
        return 4
    elif pollution_score >= 2:
        return 3
    elif pollution_score >= 1:
        return 2
    else:
        return 1

# 计算污染等级
df["level"] = df.apply(calculate_pollution_level, axis=1)

# 写入到CSV文件
df.to_csv("water_quality.csv", index=False)
