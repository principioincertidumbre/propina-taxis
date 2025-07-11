from src.features import build_features
from src.data import dataset
from src.modeling import predict

taxi_feb = dataset.read_dataframe('https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2020-02.parquet')

features = build_features.build_features()

target_col = "high_tip"

taxi_test = dataset.preprocess(df=taxi_feb, target_col=target_col)

y_pred = predict.model_predict(taxi_test, features)

f1 = predict.model_evaluate(taxi_test,target_col, y_pred)

print(f'F1 score febrero 2020: {f1}')
