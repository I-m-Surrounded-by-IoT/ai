import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout
from keras.callbacks import EarlyStopping
import joblib

# 加载数据
data = pd.read_csv("water_quality.csv")

# 保存 expected_columns
with open("expected_columns.txt", "w") as f:
    for column in data.columns:
        f.write(column + "\n")

data["date"] = pd.to_datetime(data["date"])
data = data.set_index("date")

# 数据预处理
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# 创建训练集和测试集
train_size = int(len(scaled_data) * 0.8)
train, test = (
    scaled_data[0:train_size, :],
    scaled_data[train_size : len(scaled_data), :],
)


# 创建用于训练和测试的数据集
def create_dataset(dataset, look_back=1, forecast_horizon=1):
    X, Y = [], []
    for i in range(len(dataset) - look_back - forecast_horizon):
        a = dataset[i : (i + look_back), :]
        X.append(a)
        Y.append(dataset[(i + look_back) : (i + look_back + forecast_horizon), :])
    return np.array(X), np.array(Y)


look_back = 3
forecast_horizon = 24
X_train, Y_train = create_dataset(train, look_back, forecast_horizon)
X_test, Y_test = create_dataset(test, look_back, forecast_horizon)

# 创建和训练LSTM网络
model = Sequential()
model.add(
    LSTM(50, return_sequences=True, input_shape=(X_train.shape[1], X_train.shape[2]))
)
model.add(Dropout(0.2))
model.add(LSTM(50, return_sequences=False))
model.add(Dropout(0.2))
model.add(Dense(forecast_horizon * Y_train.shape[2]))  # 修改输出层的神经元数量
model.compile(loss="mean_squared_error", optimizer="adam")

# 定义早停
early_stopping = EarlyStopping(monitor="val_loss", patience=10)

# 训练模型并进行交叉验证
model.fit(
    X_train,
    Y_train.reshape(Y_train.shape[0], -1),  # 修改Y_train的形状以匹配模型的输出
    epochs=100,
    batch_size=1,
    verbose=2,
    validation_split=0.2,
    callbacks=[early_stopping],
)

model.save("model.keras")
joblib.dump(scaler, "scaler.pkl")
