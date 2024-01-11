from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'key'


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


jogo_um = Jogo('Tetris', 'Puzzle', 'Atari')
jogo_dois = Jogo('God Of War', 'Rack in Slash', 'PS2')
jogo_tres = Jogo('Mortal Kombat', 'Luta', 'PS2')

lista_jogos = [jogo_um, jogo_dois, jogo_tres]


@app.route('/inicio')
def inicio():
    return render_template('lista.html', titulo='Jogos', jogos=lista_jogos)


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=novo')
    return render_template('novo.html', titulo='Novo jogo')


@app.route('/criar', methods=['POST', ])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    jogo = Jogo(nome, categoria, console)
    lista_jogos.append(jogo)

    return redirect('/')


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    usuario = request.form['usuario']
    senha = request.form['senha']
    if 'alohomora' == senha and 'root' == usuario:
        session['usuario_logado'] = usuario
        flash(f'Usuario {usuario} logado com sucesso!')
        proxima_pagina = request.form['proxima']
        if proxima_pagina == 'novo':
            return redirect('/novo')
        else:
            return redirect('/inicio')
    else:
        flash(f'Usuario {usuario} não existe ou a senha está incorreta!')
        return redirect('/login')


@app.route('/loggout')
def loggout():
    session['usuario_logado'] = None
    flash('Loggout efetuado com sucesso!')
    return redirect('/inicio')


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


app.run(debug=True)
