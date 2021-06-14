from flask import Flask, render_template, jsonify, request, redirect, url_for

app = Flask(__name__)

contatos = [
    {'nome': 'Fulano', 'telefone': '123123123'},
    {'nome': 'Ciclano', 'telefone': '423234234'},
    {'nome': 'Beltrano', 'telefone': '6787687686'}
]

@app.route('/')
def hello():
    # contatos = SELECT ...
    # abre conexão, executa SQL, fecha conexão
    return render_template("index.html", contatos=contatos, quantidade=len(contatos))

@app.route('/create')
def create():
    return render_template("create.html")

@app.route('/save', methods=['POST'])
def save():
    nome = request.form['nome']
    telefone = request.form['telefone']

    novo_contato = {'nome': nome, 'telefone': telefone}
    # abre conexão, executa SQL insert, fecha conexão
    contatos.append(novo_contato) # INSERT INTO contatos VALUES (...)

    return redirect("https://5000-turquoise-pinniped-63qr3oo1.ws-us09.gitpod.io")

if __name__ == '__main__':
    app.run(debug=True)
