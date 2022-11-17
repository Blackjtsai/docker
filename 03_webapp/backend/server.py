from flask import Flask
# from flask_cors import CORS  # need to mention
import json
import os

app = Flask(__name__)
# CORS(app)


@app.route("/")
def index():
    return "Hello, index!"


@app.route("/book")
def book():
    file_path = os.path.join(os.getcwd(), '03_webapp', 'backend', 'data.json')
    with open(file_path) as file:
        data = json.load(file)
    return data


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5009)
