from flask import Flask, jsonify
import os
import socket
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>q</h1>'


@app.route('/ticket', methods=['POST'])
def ticket():
    language = request.args.get('language')

    # if key doesn't exist, returns a 400, bad request error
   
    return language
    





if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
