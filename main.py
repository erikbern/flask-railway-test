from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
    return "<blink>Hello, world!</blink"


if __name__ == '__main__':
    app.run(port=os.getenv("PORT", default=5000))
