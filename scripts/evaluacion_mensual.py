from src.features import build_features
from src.data import dataset
from src.modeling import predict

taxi_jan = dataset.read_dataframe('https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2020-01.parquet')

features = build_features.build_features()

target_col = "high_tip"

taxi_jan = dataset.preprocess(df=taxi_jan, target_col=target_col)

ejemplos_jan = len(taxi_jan.index)

print(f'Cantidad de ejemplos enero 2020: {ejemplos_jan}')

y_pred = predict.model_predict(taxi_jan, features)

f1 = predict.model_evaluate(taxi_jan,target_col, y_pred)

print(f'F1 score enero 2020: {f1}')

taxi_feb = dataset.read_dataframe('https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2020-02.parquet')

taxi_feb = dataset.preprocess(df=taxi_feb, target_col=target_col)

ejemplos_feb = len(taxi_feb.index)

print(f'Cantidad de ejemplos febrero 2020: {ejemplos_feb}')

y_pred = predict.model_predict(taxi_feb, features)

f1 = predict.model_evaluate(taxi_feb,target_col, y_pred)

print(f'F1 score febrero 2020: {f1}')

taxi_mar = dataset.read_dataframe('https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2020-03.parquet')

taxi_mar = dataset.preprocess(df=taxi_mar, target_col=target_col)

ejemplos_mar = len(taxi_mar.index)

print(f'Cantidad de ejemplos marzo 2020: {ejemplos_mar}')

y_pred = predict.model_predict(taxi_mar, features)

f1 = predict.model_evaluate(taxi_mar,target_col, y_pred)

print(f'F1 score marzo 2020: {f1}')

taxi_apr = dataset.read_dataframe('https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2020-04.parquet')

taxi_apr = dataset.preprocess(df=taxi_apr, target_col=target_col)

ejemplos_apr = len(taxi_apr.index)

print(f'Cantidad de ejemplos abril 2020: {ejemplos_apr}')

y_pred = predict.model_predict(taxi_apr, features)

f1 = predict.model_evaluate(taxi_apr,target_col, y_pred)

print(f'F1 score abril 2020: {f1}')

taxi_may = dataset.read_dataframe('https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2020-05.parquet')

taxi_may = dataset.preprocess(df=taxi_may, target_col=target_col)

ejemplos_may = len(taxi_may.index)

print(f'Cantidad de ejemplos mayo 2020: {ejemplos_may}')

y_pred = predict.model_predict(taxi_may, features)

f1 = predict.model_evaluate(taxi_may,target_col, y_pred)

print(f'F1 score mayo 2020: {f1}')

taxi_jun = dataset.read_dataframe('https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2020-06.parquet')

taxi_jun = dataset.preprocess(df=taxi_jun, target_col=target_col)

ejemplos_jun = len(taxi_jun.index)

print(f'Cantidad de ejemplos junio 2020: {ejemplos_jun}')

y_pred = predict.model_predict(taxi_jun, features)

f1 = predict.model_evaluate(taxi_jun,target_col, y_pred)

print(f'F1 score junio 2020: {f1}')
