import pandas as pd

def preprocess(df, target_col):

# Basic cleaning
df = df[df['fare_amount'] > 0].reset_index(drop=True)  # avoid divide-by-zero
# add target
df['tip_fraction'] = df['tip_amount'] / df['fare_amount']
df[target_col] = df['tip_fraction'] > 0.2

# add features
df['pickup_weekday'] = df['tpep_pickup_datetime'].dt.weekday
df['pickup_hour'] = df['tpep_pickup_datetime'].dt.hour
df['pickup_minute'] = df['tpep_pickup_datetime'].dt.minute
df['work_hours'] = (df['pickup_weekday'] >= 0) & (df['pickup_weekday'] <= 4) & (df['pickup_hour'] >= 8) & (df['pickup_hour'] <= 18)
df['trip_time'] = (df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']).dt.seconds
df['trip_speed'] = df['trip_distance'] / (df['trip_time'] + EPS)

# drop unused columns
df = df[['tpep_dropoff_datetime'] + features + [target_col]]
df[features + [target_col]] = df[features + [target_col]].astype("float32").fillna(-1.0)

# convert target to int32 for efficiency (it's just 0s and 1s)
df[target_col] = df[target_col].astype("int32")

return df.reset_index(drop=True)

taxi = pd.read_parquet('https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2020-01.parquet')

target_col = "high_tip"

taxi_train = preprocess(df=taxi, target_col=target_col)
