from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={
     r"/.*": {"origins": ["http://127.0.0.1", "http://www.example.com"]}})


@app.route("/")
def helloWorld():
    return "Hello"
