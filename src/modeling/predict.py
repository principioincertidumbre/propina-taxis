from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score
import joblib

def model_predict(df, features, target_col):
    loaded_rfc = joblib.load("random_forest.joblib")
    preds_test = loaded_rfc.predict_proba(df[features])
    preds_test_labels = [p[1] for p in preds_test.round()]
    print(f'F1: {f1_score(df[target_col], preds_test_labels)}')
    return
