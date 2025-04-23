from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

command = None

@app.route("/send", methods=["POST"])
def send():
    global command
    data = request.get_json()
    if not data or 'cmd' not in data: return 'bad request', 400
    command = data['cmd']
    return 'ok'

@app.route("/get", methods=["GET"])
def get():
    global command
    c = command
    command = None
    return jsonify({'cmd': c if c else ''})

app.run(host='0.0.0.0', port=5000)
