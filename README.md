# Defect Predictor
Enterprise AI-Based Software Defect Prediction System.

This repository contains two main project folders:

1. `defect_prediction_backend/`: Python Flask REST API backend with Scikit-learn Machine Learning pipeline.
2. `DefectPredictorApp/`: Complete Android Studio project built with Kotlin, Jetpack Compose, Material 3, and Retrofit.

## Quick Execution

### Python Backend
```bash
cd defect_prediction_backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python ml/train_model.py
python app.py
```

### Android App
1. Open `DefectPredictorApp/` in Android Studio.
2. Sync Gradle files.
3. Configure your backend URL in `RetrofitClient.kt`.
4. Run on Emulator or Physical Phone.
