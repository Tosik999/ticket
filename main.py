from flask import Flask, jsonify, request
import os
import socket
import requests
from bs4 import BeautifulSoup


app = Flask(__name__)





@app.route('/')
def index():
    return '<h1>q</h1>'


@app.route('/ticket')
def ticket():
    date = request.args.get('date')
    route = request.args.get('route')
    passengers = request.args.get('passengers')
    
   
    return date, route, passengers
    





if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
