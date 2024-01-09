from flask import Flask, render_template

app = Flask(__name__)


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


@app.route('/inicio')
def ola():
    jogo_um = Jogo('Tetris', 'Puzzle', 'Ataru')
    jogo_dois = Jogo('God Of War', 'Rack in Slash', 'PS2')
    jogo_tres = Jogo('Mortal Kombat', 'Luta', 'PS2')

    lista_jogos = [jogo_um, jogo_dois, jogo_tres]

    return render_template('lista.html', titulo='Jogos', jogos=lista_jogos)


app.run()
