import os
import joblib
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix

FEATURE_COLUMNS = ['loc', 'cyclomatic_complexity', 'num_methods', 'num_classes', 'code_churn', 'num_changes', 'num_previous_defects']

def train_and_compare():
    np.random.seed(42)
    n = 1000
    df = pd.DataFrame({
        'loc': np.random.randint(20, 800, n),
        'cyclomatic_complexity': np.random.randint(1, 45, n),
        'num_methods': np.random.randint(1, 30, n),
        'num_classes': np.random.randint(1, 5, n),
        'code_churn': np.random.randint(5, 400, n),
        'num_changes': np.random.randint(1, 35, n),
        'num_previous_defects': np.random.randint(0, 8, n)
    })
    logits = (df['cyclomatic_complexity'] > 12)*1.3 + (df['loc'] > 250)*1.1 + (df['num_previous_defects'] >= 2)*1.6
    df['defective'] = (logits + np.random.normal(0, 1, n) > 2.0).astype(int)

    X = df[FEATURE_COLUMNS]
    y = df['defective']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    X_test_s = scaler.transform(X_test)

    rf = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
    rf.fit(X_train_s, y_train)
    preds = rf.predict(X_test_s)
    probs = rf.predict_proba(X_test_s)[:, 1]

    os.makedirs('saved_models', exist_ok=True)
    joblib.dump({'model': rf, 'scaler': scaler, 'features': FEATURE_COLUMNS, 'model_name': 'Random Forest'}, 'saved_models/best_defect_model.pkl')
    print(f"Random Forest F1: {f1_score(y_test, preds):.3f} | AUC: {roc_auc_score(y_test, probs):.3f}")

if __name__ == '__main__':
    train_and_compare()
