import pandas as pd

def read_dataframe(url):
    df=pd.read_parquet(url)
    return df


def preprocess(df, target_col):

    # Basic cleaning
    df = df[df['fare_amount'] > 0].reset_index(drop=True)  # avoid divide-by-zero
    # add target
    df['tip_fraction'] = df['tip_amount'] / df['fare_amount']
    df[target_col] = df['tip_fraction'] > 0.2

    # add features
    EPS = 1e-7
    df['pickup_weekday'] = df['tpep_pickup_datetime'].dt.weekday
    df['pickup_hour'] = df['tpep_pickup_datetime'].dt.hour
    df['pickup_minute'] = df['tpep_pickup_datetime'].dt.minute
    df['work_hours'] = (df['pickup_weekday'] >= 0) & (df['pickup_weekday'] <= 4) & (df['pickup_hour'] >= 8) & (df['pickup_hour'] <= 18)
    df['trip_time'] = (df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']).dt.seconds
    df['trip_speed'] = df['trip_distance'] / (df['trip_time'] + EPS)

    # drop unused columns
    numeric_feat = ["pickup_weekday","pickup_hour",'work_hours',"pickup_minute","passenger_count",'trip_distance','trip_time',
    'trip_speed']
    categorical_feat = ["PULocationID","DOLocationID","RatecodeID"]
    features = numeric_feat + categorical_feat
    cols_to_keep = ['tpep_dropoff_datetime'] + features + [target_col]
    df = df[cols_to_keep]
    df[features + [target_col]] = df[features + [target_col]].astype("float32").fillna(-1.0)

    # convert target to int32 for efficiency (it's just 0s and 1s)
    df[target_col] = df[target_col].astype("int32")

    return df.reset_index(drop=True)


def dataframe(list1,list2,list3):
    df = pd.DataFrame(list(zip(list1, list2, list3)),
         columns =['Mes', 'Cantidad ejemplos', 'F1-score']) # crea dataframe que contiene los resultados de la evaulación del modelo
    return df
