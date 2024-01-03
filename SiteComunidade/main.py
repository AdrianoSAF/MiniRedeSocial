from flask import Flask, render_template


app = Flask(__name__)



@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/usuarios")
def usuarios():
    lista_usuarios = ['Lira', 'Alon', 'Alessandra', 'Amanda']
    return render_template("usuarios.html", lista_usuarios=lista_usuarios)


if __name__ == '__main__':
    app.run(debug=True)