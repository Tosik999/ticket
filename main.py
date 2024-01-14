from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)


@app.route('/ticket')
def ticket():
    return <h1>d</h1>
    





if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
