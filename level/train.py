import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import f1_score, make_scorer
from sklearn.model_selection import TimeSeriesSplit, RandomizedSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.pipeline import Pipeline
import joblib

MAX_ITER = 3000
TOL = 1e-4
LEARNING_RATE_INIT = 0.001
RANDOM_STATE = 42
N_SPLITS = 5
TEST_SIZE = 0.2

# 加载数据
data = pd.read_csv("water_quality.csv")

data = data.drop(columns="date")

# 分离特征和目标
target = data["level"]
features = data.drop("level", axis=1)

# 保存 expected_columns
with open("expected_level_columns.txt", "w") as f:
    for column in features.columns:
        f.write(column + "\n")

# 按时间顺序划分训练集和测试集
test_size = int(len(data) * TEST_SIZE)
features_train, features_test = features[:-test_size], features[-test_size:]
target_train, target_test = target[:-test_size], target[-test_size:]

# 创建多层感知器分类器
clf = MLPClassifier(
    max_iter=MAX_ITER,
    tol=TOL,
    learning_rate_init=LEARNING_RATE_INIT,
    random_state=RANDOM_STATE,
)

# 设置交叉验证
tscv = TimeSeriesSplit(n_splits=N_SPLITS)

# 设置随机搜索参数
param_dist = {
    "hidden_layer_sizes": [(50,), (100,), (200,)],
    "activation": ["relu", "tanh", "logistic"],
}

# 设置随机搜索
random_search = RandomizedSearchCV(
    estimator=clf,
    param_distributions=param_dist,
    cv=tscv,
    scoring=make_scorer(f1_score, average="weighted"),  # 使用加权F1分数作为评估指标
    n_iter=9,  # 设置迭代次数
    random_state=RANDOM_STATE,
)

# 特征缩放
scaler = StandardScaler()

# 特征选择
selector = SelectFromModel(ExtraTreesClassifier(n_estimators=100))

# 创建管道
pipeline = Pipeline(
    [("scaler", scaler), ("selector", selector), ("classifier", random_search)]
)

# 进行随机搜索
pipeline.fit(features_train, target_train)

# 预测测试集
predictions = pipeline.predict(features_test)

# 计算F1分数
f1 = f1_score(y_true=target_test, y_pred=predictions, average="weighted")

print(f"模型的F1分数为：{f1}")

# 保存模型
joblib.dump(pipeline, "water_quality_level.joblib")

# 加载模型
loaded_pipeline = joblib.load("water_quality_level.joblib")

# 使用加载的模型进行预测
loaded_predictions = loaded_pipeline.predict(features_test)

# 验证加载的模型的F1分数
loaded_f1 = f1_score(y_true=target_test, y_pred=loaded_predictions, average="weighted")

print(f"加载的模型的F1分数为：{loaded_f1}")
