import pandas as pd
import numpy as np

np.random.seed(42)

# 生成数据
data = pd.DataFrame(
    {
        "temperature": np.random.normal(20, 1, 5),  # 温度
        "ph": np.random.normal(7, 3, 5),  # pH值
        "level": [0, 1, 2, 3, 4],  # 污染等级
    },
    columns=["temperature", "ph", "level"],
)

data.to_csv("water_quality_level.csv", index=False)

for i in range(99):
    new_data = data.copy()
    new_data.iloc[:, 0] = np.random.normal(20, 1, 5)
    new_data["level"] = new_data.apply(lambda x: int(abs(x["ph"] - 7)), axis=1)
    new_data.to_csv("water_quality_level.csv", mode="a", header=False, index=False)
