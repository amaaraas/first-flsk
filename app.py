from flask import Flask 

app = Flask(__name__)

@app.route("/")
def saludinho():
    return "<h1><center>Ola ke aze (titulo super etico y profesional)<center><h1>" 


@app.route("/bye")
def despedida():
    return "<h1><center>Buenos dias, buenas tardes, buenas noches. Que le vaya wonito<center><h1>" 