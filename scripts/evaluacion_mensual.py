from src.features import build_features
from src.data import dataset
from src.modeling import predict
from src.visualization import plots

# Crea listas para almacenar resultados
meses = []

ejemplos_mensual = []

f1_mensual = []

# Evaluación mensual datos viajes taxis amarillos Nueva York
taxi_jan = dataset.read_dataframe('https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2020-01.parquet')

features = build_features.build_features()

target_col = "high_tip"

taxi_jan = dataset.preprocess(df=taxi_jan, target_col=target_col)

ejemplos_jan = len(taxi_jan.index)  # Calcula cantidad ejemplos mensuales

ejemplos_mensual.append(ejemplos_jan)

meses.append('Enero')

print(f'Cantidad de ejemplos enero 2020: {ejemplos_jan}')

y_pred = predict.model_predict(taxi_jan, features)

f1 = predict.model_evaluate(taxi_jan,target_col, y_pred)

print(f'F1 score enero 2020: {f1}')

f1_mensual.append(f1)

# Evaluación febrero 2020
taxi_feb = dataset.read_dataframe('https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2020-02.parquet')

taxi_feb = dataset.preprocess(df=taxi_feb, target_col=target_col)

ejemplos_feb = len(taxi_feb.index)  # Calcula cantidad ejemplos mensuales

print(f'Cantidad de ejemplos febrero 2020: {ejemplos_feb}')

ejemplos_mensual.append(ejemplos_feb)

meses.append('Febrero')

y_pred = predict.model_predict(taxi_feb, features)

f1 = predict.model_evaluate(taxi_feb,target_col, y_pred)

print(f'F1 score febrero 2020: {f1}')

f1_mensual.append(f1)

# Evaluación marzo 2020
taxi_mar = dataset.read_dataframe('https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2020-03.parquet')

taxi_mar = dataset.preprocess(df=taxi_mar, target_col=target_col)

ejemplos_mar = len(taxi_mar.index) # Calcula cantidad ejemplos mensuales

meses.append('Marzo')

print(f'Cantidad de ejemplos marzo 2020: {ejemplos_mar}')


ejemplos_mensual.append(ejemplos_mar) # Calcula cantidad ejemplos mensuales

y_pred = predict.model_predict(taxi_mar, features)

f1 = predict.model_evaluate(taxi_mar,target_col, y_pred)

print(f'F1 score marzo 2020: {f1}')

f1_mensual.append(f1)

# Evaluación abril 2020
taxi_apr = dataset.read_dataframe('https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2020-04.parquet')

taxi_apr = dataset.preprocess(df=taxi_apr, target_col=target_col)

ejemplos_apr = len(taxi_apr.index) # Calcula cantidad ejemplos mensuales

meses.append('Abril')

print(f'Cantidad de ejemplos abril 2020: {ejemplos_apr}')

ejemplos_mensual.append(ejemplos_apr)

y_pred = predict.model_predict(taxi_apr, features)

f1 = predict.model_evaluate(taxi_apr,target_col, y_pred)

print(f'F1 score abril 2020: {f1}')

f1_mensual.append(f1)

# Evaluación mayo 2020
taxi_may = dataset.read_dataframe('https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2020-05.parquet')

taxi_may = dataset.preprocess(df=taxi_may, target_col=target_col)

ejemplos_may = len(taxi_may.index) # Calcula cantidad ejemplos mensuales

meses.append('Mayo')

print(f'Cantidad de ejemplos mayo 2020: {ejemplos_may}')


ejemplos_mensual.append(ejemplos_may)

y_pred = predict.model_predict(taxi_may, features)

f1 = predict.model_evaluate(taxi_may,target_col, y_pred)

print(f'F1 score mayo 2020: {f1}')

f1_mensual.append(f1)

# Evaluación junio 2020
taxi_jun = dataset.read_dataframe('https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2020-06.parquet')

taxi_jun = dataset.preprocess(df=taxi_jun, target_col=target_col)

ejemplos_jun = len(taxi_jun.index) # Calcula cantidad ejemplos mensuales

meses.append('Junio')

print(f'Cantidad de ejemplos junio 2020: {ejemplos_jun}')

ejemplos_mensual.append(ejemplos_jun)

y_pred = predict.model_predict(taxi_jun, features)

f1 = predict.model_evaluate(taxi_jun,target_col, y_pred)

print(f'F1 score junio 2020: {f1}')

f1_mensual.append(f1)

# Procesa resultados evaluaciones mensuales
result_eval = dataset.dataframe(meses,ejemplos_mensual, f1_mensual) # crea dataframe resultados

print(result_eval)

# Gráficos resultados
plots.lineplot(result_eval, meses, ejemplos_mensual, "Mes", "Cantidad viajes", "Cantidad viajes taxis amarillos Nueva York enero-junio 2020")

plots.lineplot(result_eval, meses, f1_mensual, "Mes", "F1-score", "F1-score enero-junio 2020")

