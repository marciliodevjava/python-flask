from flask import Flask, render_template, request, redirect, session, flash, url_for

app = Flask(__name__)
app.secret_key = 'key'


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


class Usuario:
    def __init__(self, nome, senha, nickname):
        self.nome = nome
        self.senha = senha
        self.nickname = nickname


usuario = Usuario('marcilio', '123456', 'marcilio')
usuario1 = Usuario('Pedro', '12345', 'pedro')
usuario2 = Usuario('Jose', '1234', 'jose')
usuario3 = Usuario('João', '123', 'joao')

usuario_list = {usuario.nickname: usuario,
                usuario1.nickname: usuario1,
                usuario2.nickname: usuario2,
                usuario3.nickname: usuario3}

jogo_um = Jogo('Tetris', 'Puzzle', 'Atari')
jogo_dois = Jogo('God Of War', 'Rack in Slash', 'PS2')
jogo_tres = Jogo('Mortal Kombat', 'Luta', 'PS2')

lista_jogos = [jogo_um, jogo_dois, jogo_tres]


@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista_jogos)


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo jogo')


@app.route('/criar', methods=['POST', ])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    jogo = Jogo(nome, categoria, console)
    lista_jogos.append(jogo)

    return redirect(url_for('index'))


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    solicitacao = request.form['usuario']
    if request.form['usuario'] in usuario_list:
        usua = usuario_list[request.form['usuario']]
        if request.form['senha'] == usua.senha:
            session['usuario_logado'] = usua.nickname
            flash(f'Usuario {usua.nickname} logado com sucesso!')
            proxima_pagina = request.form['proxima']
            if proxima_pagina == 'novo':
                return redirect(url_for('novo'))
            else:
                return redirect(url_for('index'))
    else:
        flash(f'Usuario {solicitacao} não existe ou a senha está incorreta!')
        return redirect(url_for('login'))


@app.route('/loggout')
def loggout():
    session['usuario_logado'] = None
    flash('Loggout efetuado com sucesso!')
    return redirect(url_for('index'))


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


app.run(debug=True)
