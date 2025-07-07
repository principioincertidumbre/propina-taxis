from src.features import build_features
from src.data import dataset
from src.modeling import train

taxi=dataset.read_dataframe('https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2020-01.parquet')

features = build_features.build_features()

target_col = "high_tip"

taxi_train = dataset.preprocess(df=taxi, target_col=target_col)

train.train_model(taxi_train, features, target_col)

