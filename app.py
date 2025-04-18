from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Witaj w moim API!"})

@app.route('/mojastrona')
def mojastrona():
    return "To jest moja strona!"

@app.route('/hello')
def hello():
    name = request.args.get("name")
    if name:
        return f"Hello {name}!"
    else:
        return "Hello!"

@app.route('/api/v1.0/predict')
def predict():
    try:
        num1 = float(request.args.get("num1", 0))
        num2 = float(request.args.get("num2", 0))
    except (ValueError, TypeError):
        return jsonify({"error": "Bad Request"}), 400

    suma = num1 + num2
    prediction = 1 if suma > 5.8 else 0

    return jsonify({
        "prediction": prediction,
        "features": {
            "num1": num1,
            "num2": num2
        }
    })

# Obsługa błędu 404 – brak strony
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not Found"}), 404

# Obsługa błędu 400 – złe dane wejściowe
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request"}), 400

if __name__ == '__main__':
    app.run()
