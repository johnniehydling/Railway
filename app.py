from flask import Flask, Response

app = Flask(__name__)

@app.route('/answer', methods=['POST'])
def answer():
    xml = '''<?xml version="1.0" encoding="UTF-8"?>
    <Response>
        <Play digits="5"/>
    </Response>'''
    return Response(xml, mimetype='text/xml')
```

**`requirements.txt`**
```
flask
gunicorn
```

**`Procfile`**
```
web: gunicorn app:app
