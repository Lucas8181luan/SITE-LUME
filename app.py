from flask import Flask, render_template, request

app = Flask(__name__)

joias = [
    {
        'id': 1,
        'nome': 'Anel Prisma',
        'imagem': '/static/anel_prisma.png',
        'descricao': 'Tamanho 22',
        'preco': 'R$ 109,90'
    },
    {
        'id': 2,
        'nome': 'Anel Aurora Rosa',
        'imagem': '/static/anel_aurora_rosa.png',
        'descricao': 'Tamanho 17',
        'preco': 'R$ 129,90'
    },
    {
        'id': 3,
        'nome': 'Anel Solitário Lumiere',
        'imagem': '/static/anel_solitario_lumiere.png',
        'descricao': 'Tamanho 23',
        'preco': 'R$ 109,90'
    },
    {
        'id': 4,
        'nome': 'Anel Harmonia',
        'imagem': '/static/anel_harmonia.png',
        'descricao': 'Tamanho 18',
        'preco': 'R$ 119,90'
    },
    {
        'id': 5,
        'nome': 'Anel Lume',
        'imagem': '/static/anel_lume.png',
        'descricao': 'Tamanho 21',
        'preco': 'R$ 109,90'
    },
    {
        'id': 6,
        'nome': 'Colar Gotas Lume',
        'imagem': '/static/colar_gotas_lume.png',
        'descricao': '',
        'preco': 'R$ 139,90'
    },
    {
        'id': 7,
        'nome': 'Colar Pedras Rosas',
        'imagem': '/static/colar_pedras_rosas.png',
        'descricao': '',
        'preco': 'R$ 139,90'
    },
    {
        'id': 8,
        'nome': 'Colar Árvore da Vida',
        'imagem': '/static/colar_arvore_da_vida.png',
        'descricao': '',
        'preco': 'R$ 149,90'
    },
    {
        'id': 9,
        'nome': 'Colar Estrela Lume',
        'imagem': '/static/colar_estrela_lume.png',
        'descricao': '',
        'preco': 'R$ 149,90'
    },
    {
        'id': 10,
        'nome': 'Conjunto Ponto de Luz',
        'imagem': '/static/conjunto_ponto_de_luz.png',
        'descricao': '',
        'preco': 'R$ 179,90'
    },
    {
        'id': 11,
        'nome': 'Pulseira Corações e Luz',
        'imagem': '/static/pulseira_coracoes_e_luz.png',
        'descricao': '',
        'preco': 'R$ 69,90'
    },
    {
        'id': 12,
        'nome': 'Pulseira Gotas de Luz Rosa',
        'imagem': '/static/pulseira_gotas_de_luz_rosa.png',
        'descricao': '',
        'preco': 'R$ 79,90'
    },
    {
        'id': 13,
        'nome': 'Pulseira Trevo Preto',
        'imagem': '/static/pulseira_trevo_preto.png',
        'descricao': '',
        'preco': 'R$ 159,90'
    },
    {
        'id': 14,
        'nome': 'Pulseira Trevo Branco',
        'imagem': '/static/pulseira_trevo_branco.png',
        'descricao': '',
        'preco': 'R$ 159,90'
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
