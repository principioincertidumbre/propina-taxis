from sklearn.ensemble import RandomForestClassifier

taxi_train = taxi_train.head(100000)

rfc = RandomForestClassifier(n_estimators=100, max_depth=10)

rfc.fit(taxi_train[features], taxi_train[target_col])
