from flask import Flask, Response
import os

app = Flask(__name__)

@app.route('/')
def health():
    return 'OK', 200

@app.route('/answer', methods=['POST'])
def answer():
    xml = '''<?xml version="1.0" encoding="UTF-8"?>
    <Response>
        <Play digits="5"/>
    </Response>'''
    return Response(xml, mimetype='text/xml')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
