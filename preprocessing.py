import pandas as pd
import numpy as np

FEATURE_COLUMNS = ['loc', 'cyclomatic_complexity', 'num_methods', 'num_classes', 'code_churn', 'num_changes', 'num_previous_defects']

def map_and_clean_dataset(df: pd.DataFrame, missing_strategy='median'):
    clean = pd.DataFrame()
    for col in FEATURE_COLUMNS:
        if col in df.columns:
            clean[col] = pd.to_numeric(df[col], errors='coerce')
        else:
            clean[col] = 100 if col == 'loc' else 8 if col == 'cyclomatic_complexity' else 0
    if missing_strategy == 'median':
        clean = clean.fillna(clean.median())
    elif missing_strategy == 'mean':
        clean = clean.fillna(clean.mean())
    elif missing_strategy == 'zero':
        clean = clean.fillna(0)
    return clean
