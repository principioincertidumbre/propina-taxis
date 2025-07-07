from src.features import build_features
from src.data import dataset
from src.modeling import predict

taxi_feb = dataset.read_dataframe('https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2020-02.parquet')

features = build_features.build_features()

target_col = "high_tip"

taxi_test = dataset.preprocess(df=taxi_feb, target_col=target_col)

predict.model_predict(taxi_test, features, target_col)
