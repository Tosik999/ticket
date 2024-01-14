from flask import Flask, jsonify, request
import os
import socket


app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>q</h1>'


@app.route('/ticket')
def ticket():
    language = request.args.get('language')
   
    return language
    





if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
