from flask import Flask, Response, jsonify
import os

app = Flask(__name__)

@app.route('/')
def health():
    return 'OK', 200

@app.route('/answer', methods=['POST'])
def answer():
    response = {
        "play": "sound/dtmf/5"
    }
    return jsonify(response)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
