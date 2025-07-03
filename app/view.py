from app import app
from flask import render_template

@app.route('/')
def homepage():
    nome = "kotryk"
    idade = 17
    interesses = ["Programação", "Música", "Jogos"]

    dicionario = {
        'nome': nome,
        'idade': idade,
        'interesses': interesses
    }
    return render_template('index.html', dicionario=dicionario)

@app.route('/sobre/')
def sobre():
    return render_template('sobre.html')


@app.route('/contato/')
def novapagina():
    context={}
    if request.args.get('pesquisa') != '':
        pesquisa = request.args.get('pesquisa')

    context.update({'pesquisa': pesquisa})
    return render_template('contato.html', context)
