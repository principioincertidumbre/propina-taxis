from sklearn.ensemble import RandomForestClassifier
import joblib

'''Función para entrenar modelo'''
def train_model(df, features, target_col):
    df_train = df.head(42120000) # Representa aproximadamente un 66% del dataset de enero 2020
    rfc = RandomForestClassifier(n_estimators=100, max_depth=10)
    rfc.fit(df_train[features], df_train[target_col])
    joblib.dump(rfc, "models/random_forest.joblib") # Guarda modelo entrenado
    return




