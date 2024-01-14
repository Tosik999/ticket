from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)


@app.route('/ticket')
def ticket():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("https://flask-production-eeed.up.railway.app/ticket", 5000)
    server_socket.bind(server_address)
    server_socket.listen(1)

    response = "Привет от сервера!"
    client_socket.send(response.encode())





if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
