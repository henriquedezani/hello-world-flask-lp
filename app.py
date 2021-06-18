from flask import Flask, render_template, jsonify, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def create_database():
    conn = sqlite3.connect('agenda.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS Contatos(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, nome VARCHAR NOT NULL, telefone VARCHAR NOT NULL)""")
    conn.close()

@app.route('/')
def hello():
    # contatos = SELECT ...
    # abre conexão, executa SQL, fecha conexão
    conn = sqlite3.connect('agenda.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM Contatos """)
    contatos = cursor.fetchall()        
    return render_template("index.html", contatos=contatos, quantidade=len(contatos))
    conn.close()

@app.route('/create')
def create():
    return render_template("create.html")

@app.route('/save', methods=['POST'])
def save():
    nome = request.form['nome']
    telefone = request.form['telefone']

    # novo_contato = {'nome': nome, 'telefone': telefone}
    # contatos.append(novo_contato) # INSERT INTO contatos VALUES (...)
    # abre conexão, executa SQL insert, fecha conexão
    conn = sqlite3.connect('agenda.db')
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO Contatos(nome, telefone) VALUES(?, ?) """, (nome, telefone))
    conn.commit()

    return redirect("/")

if __name__ == '__main__':
    create_database()
    app.run(debug=True)
