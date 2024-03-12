from flask import Flask, jsonify
import os

app = Flask(__name__)
val = 0


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask application"})

@app.route('/value')
def value():
    global  val
    val = val + 1
    return val


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
