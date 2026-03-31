from flask import Flask, jsonify
import os
import requests

app = Flask(__name__)

PUSHOVER_TOKEN = "ajgbvbmr51ash8b4xbf2qpxx3ei28o"
PUSHOVER_USER = "u9cmpck4su5zv28x9se3qtw9d6vd8g"

def send_push():
    requests.post(
        "https://api.pushover.net/1/messages.json",
        data={
            "token": PUSHOVER_TOKEN,
            "user": PUSHOVER_USER,
            "message": "Dörren har öppnats! 🚪",
            "title": "Porttelefon"
        }
    )

@app.route('/')
def health():
    return 'OK', 200

@app.route('/answer', methods=['POST'])
def answer():
    send_push()
    return jsonify({"play": "sound/dtmf/5"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
