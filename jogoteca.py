from flask import Flask, render_template, request, redirect

app = Flask(__name__)


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


jogo_um = Jogo('Tetris', 'Puzzle', 'Ataru')
jogo_dois = Jogo('God Of War', 'Rack in Slash', 'PS2')
jogo_tres = Jogo('Mortal Kombat', 'Luta', 'PS2')

lista_jogos = [jogo_um, jogo_dois, jogo_tres]


@app.route('/inicio')
def inicio():
    return render_template('lista.html', titulo='Jogos', jogos=lista_jogos)


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo jogo')


@app.route('/criar', methods=['POST', ])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    jogo = Jogo(nome, categoria, console)
    lista_jogos.append(jogo)

    return redirect('/inicio')


app.run(debug=True)
