from flask import Flask
from flask_cors import CORS  # need to mention
import json

app = Flask(__name__)
CORS(app)


@app.route("/book")
def json_file():
    file = open('./book.json')
    json_data = json_file(file)
    return "hello"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5009)