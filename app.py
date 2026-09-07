from flask import Flask, request, jsonify
import numpy as np
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Entrenamos un modelo de ejemplo (siempre el mismo para demostración)
X = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 6, 8])
model = LinearRegression().fit(X, y)


@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})


@app.route('/predict', methods=['GET'])
def predict():
    try:
        x_val = float(request.args.get('x', 0))
        prediction = model.predict([[x_val]])[0]
        return jsonify({"x": x_val, "prediction": round(prediction, 2)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    # Escuchar en todas las interfaces para que Docker pueda redirigir el tráfico
    app.run(host='0.0.0.0', port=5000)