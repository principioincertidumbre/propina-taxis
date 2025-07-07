from src.features import build_features
from src.data import dataset
from src.modeling import predict

taxi_jan = dataset.read_dataframe('https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2020-01.parquet')

features = build_features.build_features()

target_col = "high_tip"

taxi_train = dataset.preprocess(df=taxi_jan, target_col=target_col)

y_pred = predict.model_predict(taxi_train, features)

f1 = predict.model_evaluate(taxi_train,target_col, y_pred)

print(f'F1  score: {f1}')
