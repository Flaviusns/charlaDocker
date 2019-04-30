from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hola desde la charla de Docker 😀"