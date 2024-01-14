from flask import Flask, request

app = Flask(__name__)

@app.route('/endpoint', methods=['GET'])
def handle_request():
    param1 = request.args.get('date')
    param2 = request.args.get('passengers')
    param3 = request.args.get('route')
    return [param1, param2, param3]

if __name__ == '__main__':
    app.run()
