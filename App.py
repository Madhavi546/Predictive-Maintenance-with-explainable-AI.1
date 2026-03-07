from flask import Flask, request, jsonify
import joblib
import numpy as np
import shap

app = Flask(__name__)

# Load model & scaler
model = joblib.load("factoryguard_xgb_model.pkl")
scaler = joblib.load("scaler.pkl")

explainer = shap.TreeExplainer(model)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    features = np.array(data["features"]).reshape(1, -1)

    # Scale
    features_scaled = scaler.transform(features)

    # Prediction
    prob = model.predict_proba(features_scaled)[0][1]

    # SHAP explanation
    shap_values = explainer.shap_values(features)

    return jsonify({
        "failure_probability": round(float(prob), 4),
        "shap_values": shap_values[0].tolist()
    })

if __name__ == "__main__":
    app.run(debug=False)