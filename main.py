from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>q</h1>'


@app.route('/ticket')
def ticket():
    a = 'eeeeeeeeea'
    return a
    





if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
