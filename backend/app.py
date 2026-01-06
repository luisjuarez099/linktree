from flask import Flask,jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def bienvenida():
    return "Bienvenido a Flask"

@app.route("/clientes", methods=["GET"])
def clientes():
    #creamos un json 
    clientes = [
        {"id": 1, "nombre": "Juan Perez", "email": "juan.perez@example.com"},
        {"id": 2, "nombre": "Maria Garcia", "email": "maria.garcia@example.com"},
        {"id": 3, "nombre": "Carlos Lopez", "email": "carlos.lopez@example.com"},
        {"id": 4, "nombre": "Ana Martinez", "email": "ana.martinez@example.com"}
    ]

    return jsonify(clientes)
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000, debug=True)
