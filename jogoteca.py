from flask import Flask, render_template

app = Flask(__name__)


@app.route('/inicio')
def ola():
    lista_jogos = ['Tetris', 'Skytim', 'Crash']
    return render_template('lista.html', titulo='Jogos', jogos=lista_jogos)


app.run()
