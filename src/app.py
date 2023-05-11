from flask import Flask, render_template
from jinja2 import Template

app = Flask("__name__")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/home")
def home2():
    return render_template("home.html")

@app.route("/academico")
def academico():
    return render_template("academico.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

if __name__ == '__main__':
 app.run()
