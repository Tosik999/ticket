from flask import Flask, jsonify, request
import os
import socket
import requests
from bs4 import BeautifulSoup


app = Flask(__name__)





@app.route('/')
def index():
    return '<h1>q</h1>'


@app.route('/ticket', methods=['POST'])
def ticket():
    date = request.args.get('date')
    
   
    return date
    





if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
