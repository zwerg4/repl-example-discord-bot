from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')
def index():
    return 'Discord App is Running'
def run():
    app.run(host='0.0.0.0',port=8080)
