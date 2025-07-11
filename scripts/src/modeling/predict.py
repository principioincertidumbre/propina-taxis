from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score
import joblib

'''Funciones para predicciones y evaluar modelo'''
def model_predict(df, features):
    loaded_rfc = joblib.load("models/random_forest.joblib") # Carga modelo entrenadp
    preds_test = loaded_rfc.predict_proba(df[features])
    preds_test_labels = [p[1] for p in preds_test.round()]
    return preds_test_labels

def model_evaluate(df, target_col, preds_test_labels):
    F1 = f1_score(df[target_col], preds_test_labels)
    return F1


