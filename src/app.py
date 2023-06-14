from flask import Flask, render_template
from jinja2 import Template

app = Flask("__name__")


@app.route('/')
def home():
    title = "Home"
    return render_template("home.html", title=title)


@app.route('/academico')
def academico():
    title = "Acadêmico"
    return render_template("academico.html", title=title)


@app.route('/sobre')
def sobre():
    title = "Sobre mim"
    return render_template("sobre.html", title=title)


@app.route('/contatos')
def contatos():
    title = "Contatos"
    return render_template("contatos.html", title=title)


if __name__ == '__main__':
    app.run(debug=True)
