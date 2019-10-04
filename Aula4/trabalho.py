from flask import Flask, render_template, request, redirect
from models.cerveja import Cerveja

app=Flask(__name__)
lista_cervejas = []

@app.route('/')
def inicio():
    return render_template('tbl.html', titulo_pagina = 'Home')

@app.route('/listar')
def listar():
    return render_template('listar.html', titulo_pagina = 'Listar', lista = lista_cervejas)

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html', titulo_pagina = 'Cadastrar')

@app.route('/pedidos')
def pedidos():
    return render_template('pedidos.html', titulo_pagina = 'pedidos')


@app.route('/salvar', methods=['POST'])
def salvar():
    nome = request.form['nome']
    tipo = request.form['tipo']
    preco = request.form['preco']
    validade = request.form['validade']
    nova_cerveja = Cerveja(nome, tipo, preco, validade)
    lista_cervejas.append(nova_cerveja)
    return redirect('/listar')      
    
app.run()