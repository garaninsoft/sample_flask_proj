from flask import Flask
app = Flask(__name__)
@app.route('/hello')
def hello():
    return "Hello, from my first app!"

app.run(host='0.0.0.0', port=81)