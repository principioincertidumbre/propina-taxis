'''Función para definir atributos numéricos y categóricos'''

def build_features():
    numeric_feat = ["pickup_weekday",
    "pickup_hour",'work_hours',
    "pickup_minute","passenger_count",
    'trip_distance','trip_time','trip_speed']
    categorical_feat = [
    "PULocationID","DOLocationID",
    "RatecodeID"]
    features = numeric_feat + categorical_feat
    return features
