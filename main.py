from flask import Flask, jsonify
import os
import socket
import request

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>q</h1>'


@app.route('/ticket')
def ticket():
    date = request.args.get('date')
    route = request.args.get('route')
    return date, route
    





if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
