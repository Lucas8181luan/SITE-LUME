from flask import Flask, render_template, request

app = Flask(__name__)

joias = [
    {
        'id': 1,
        'nome': 'Anel Solitário',
        'imagem': '/static/anel_solitario.png',
        'descricao': 'Anel solitário com pedra brilhante.',
        'preco': 'R$ 150,00'
    },
    {
        'id': 2,
        'nome': 'Anel Prata 925',
        'imagem': '/static/anel.png',
        'descricao': 'Anel delicado em prata 925.',
        'preco': 'R$ 120,00'
    },
    {
        'id': 3,
        'nome': 'Brinco Argola',
        'imagem': '/static/brinco_angola.png',
        'descricao': 'Brinco argola em prata com design moderno.',
        'preco': 'R$ 110,00'
    },
    {
        'id': 4,
        'nome': 'Colar Coração',
        'imagem': '/static/colar_coração.png',
        'descricao': 'Colar com pingente de coração.',
        'preco': 'R$ 180,00'
    },
    {
        'id': 5,
        'nome': 'Colar Estrela',
        'imagem': '/static/colar_esterla.png',
        'descricao': 'Colar com pingente de estrela em prata.',
        'preco': 'R$ 170,00'
    },
    {
        'id': 6,
        'nome': 'Pulseira Elegante',
        'imagem': '/static/pulseira_elegante.png',
        'descricao': 'Pulseira fina e elegante.',
        'preco': 'R$ 90,00'
    }
]
@app.route('/')
def index():
    filtro = request.args.get('filtro', '')
    if filtro:
        filtradas = [j for j in joias if filtro.lower() in j['nome'].lower()]
    else:
        filtradas = joias
    return render_template('index.html', joias=filtradas, filtro=filtro)

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/joia/<int:id>')
def joia(id):
    j = next((j for j in joias if j['id'] == id), None)
    return render_template('joia.html', joia=j)

@app.route('/carrinho')
def carrinho():
    return render_template('carrinho.html')

@app.route('/home')
def home():
    return render_template('home.html')

import os
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
