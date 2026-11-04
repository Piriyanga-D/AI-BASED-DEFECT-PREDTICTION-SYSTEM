from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from datetime import datetime
from config import Config
from services.ml_service import MLService
from services.report_service import ReportService
from services.email_service import EmailService
from database.db import init_db

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

init_db(app)

ml_service = MLService()
report_service = ReportService()
email_service = EmailService()

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({
        "status": "healthy",
        "service": "Defect Predictor Backend",
        "timestamp": datetime.utcnow().isoformat()
    }), 200

@app.route('/api/auth/register', methods=['POST'])
def register():
    data = request.get_json() or {}
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    if not name or not email or not password:
        return jsonify({"error": "Missing required fields"}), 400
    return jsonify({
        "success": True,
        "token": f"jwt_{os.urandom(16).hex()}",
        "user": {"name": name, "email": email, "role": "Engineer"}
    }), 201

@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    email = data.get('email')
    password = data.get('password')
    if not email or not password:
        return jsonify({"error": "Email and password required"}), 400
    return jsonify({
        "success": True,
        "token": f"jwt_{os.urandom(16).hex()}",
        "user": {"name": email.split('@')[0].capitalize(), "email": email, "role": "Lead QA"}
    }), 200

@app.route('/api/dashboard', methods=['GET'])
def dashboard():
    return jsonify({
        "total_modules_analyzed": 15,
        "defective_modules": 7,
        "non_defective_modules": 8,
        "high_risk_modules": 5,
        "defect_rate": 46.7
    }), 200

@app.route('/api/predictions/manual', methods=['POST'])
def predict_manual():
    metrics = request.get_json() or {}
    result = ml_service.predict_single(metrics)
    return jsonify({"success": True, "prediction": result}), 200

@app.route('/api/predictions/batch', methods=['POST'])
def predict_batch():
    data = request.get_json() or {}
    modules = data.get('modules', [])
    results = ml_service.predict_batch(modules)
    return jsonify({"success": True, "count": len(results), "predictions": results}), 200

@app.route('/api/model/info', methods=['GET'])
def model_info():
    return jsonify(ml_service.get_model_info()), 200

@app.route('/api/reports/generate', methods=['POST'])
def generate_report():
    data = request.get_json() or {}
    proj = data.get('project_name', 'Audit')
    fmt = data.get('format', 'PDF')
    preds = data.get('predictions', [])
    path = report_service.generate(proj, preds, fmt)
    return jsonify({"success": True, "file_path": path}), 200

@app.route('/api/notifications/email', methods=['POST'])
def send_email():
    data = request.get_json() or {}
    res = email_service.send_report(data.get('recipient_email'), data.get('project_name'))
    return jsonify({"success": res.get('delivered', False), "data": res}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
