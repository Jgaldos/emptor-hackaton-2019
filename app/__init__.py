# app.py
from flask import Flask
from app.pe .test import test_peru
app = Flask(__name__)


@app.route('/peru')
def hello_world():
    return test_peru()


if __name__ == '__main__':
    app.run(host='0.0.0.0')