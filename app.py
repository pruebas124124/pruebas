import os

from flask import Flask, request, jsonify
import numpy as np
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Entrenamos un modelo de ejemplo (siempre el mismo para demostración)
X = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 6, 8])
model = LinearRegression().fit(X, y)


@app.route('/', methods=['GET'])
def index():
    return jsonify({
        "message": "API de regresión lineal activa",
        "endpoints": {
            "/health": "estado del servicio",
            "/predict?x=<numero>": "devuelve la predicción del modelo"
        }
    })


@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})


@app.route('/predict', methods=['GET'])
def predict():
    try:
        x_val = float(request.args.get('x', 0))
        prediction = model.predict([[x_val]])[0]
        return jsonify({"x": x_val, "prediction": round(float(prediction), 2)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Render (y la mayoría de plataformas cloud) asignan el puerto vía la
# variable de entorno PORT. Si no existe (ej. corriendo en local), usamos 5000.
# Este bloque solo se usa si ejecutas "python app.py" directamente;
# en producción lo levanta gunicorn (ver Dockerfile).
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
