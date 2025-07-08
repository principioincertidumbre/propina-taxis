from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model(df, features, target_col):
    df_train = df.head(600000)
    rfc = RandomForestClassifier(n_estimators=100, max_depth=10)
    rfc.fit(df_train[features], df_train[target_col])
    joblib.dump(rfc, "models/random_forest.joblib")
    return




