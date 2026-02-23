def finalizar():
    carrinho = session.get('carrinho', {})
    itens = []
    for id_str, qtd in carrinho.items():
        joia = next((j for j in joias if str(j['id']) == id_str), None)
        if joia:
            itens.append(f"{joia['nome']} - {joia['preco']} - Quantidade: {qtd}")
    mensagem = '\n'.join(itens)
    mensagem = f"Olá! Gostaria de finalizar a compra com os seguintes itens:\n{mensagem}"
    import urllib.parse
    msg_encoded = urllib.parse.quote(mensagem)
    whatsapp_url = f"https://wa.me/5561991580081?text={msg_encoded}"
    return redirect(whatsapp_url)
from flask import Flask, render_template, request
from flask import session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'lumejoias2026'  # chave para sessão

# ...existing code...

@app.route('/finalizar')
def finalizar():
    carrinho = session.get('carrinho', {})
    itens = []
    total = 0.0
    for id_str, qtd in carrinho.items():
        joia = next((j for j in joias if str(j['id']) == id_str), None)
        if joia:
            preco = float(joia['preco'].replace('R$', '').replace(',', '.'))
            subtotal = preco * qtd
            total += subtotal
            itens.append(f"{joia['nome']}\n\tTamanho/Descrição: {joia['descricao']}\n\tPreço unitário: {joia['preco']}\n\tQuantidade: {qtd}\n\tSubtotal: R$ {subtotal:.2f}".replace('.', ','))
    mensagem = "Olá! Gostaria de finalizar a compra com os seguintes itens:\n\n" + '\n\n'.join(itens)
    mensagem += f"\n\nTotal: R$ {total:.2f}".replace('.', ',')
    import urllib.parse
    msg_encoded = urllib.parse.quote(mensagem)
    whatsapp_url = f"https://wa.me/5561991580081?text={msg_encoded}"
    return redirect(whatsapp_url)

# Remover produto do carrinho
@app.route('/remover_carrinho/<int:id>')
def remover_carrinho(id):
    carrinho = session.get('carrinho', {})
    id_str = str(id)
    if id_str in carrinho:
        carrinho.pop(id_str)
        session['carrinho'] = carrinho
    return redirect(url_for('carrinho'))

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
    },
    {
        'id': 16,
        'nome': 'Brinco Pérola',
        'imagem': '/static/brinco_perola .png',
        'descricao': 'Quantidade: 1',
        'preco': 'R$ 29,90'
    },
    {
        'id': 17,
        'nome': 'Brinco Pérola',
        'imagem': '/static/brinco_perola_1 .png',
        'descricao': 'Quantidade: 1',
        'preco': 'R$ 29,90'
    },
    {
        'id': 18,
        'nome': 'Colar Árvore da Vida',
        'imagem': '/static/colar_arvore_da_vida.png.png',
        'descricao': 'Quantidade: 1',
        'preco': 'R$ 79,90'
    },
    {
        'id': 19,
        'nome': 'Colar Pedras Rosa',
        'imagem': '/static/colar_pedra_rosa.png',
        'descricao': 'Quantidade: 1',
        'preco': 'R$ 79,90'
    },
    {
        'id': 20,
        'nome': 'Colar Estrela Lume',
        'imagem': '/static/colar_estrela_lume.png.png',
        'descricao': 'Quantidade: 1',
        'preco': 'R$ 79,90'
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

# Adicionar produto ao carrinho
@app.route('/add_carrinho/<int:id>')
def add_carrinho(id):
    carrinho = session.get('carrinho', {})
    carrinho[str(id)] = carrinho.get(str(id), 0) + 1
    session['carrinho'] = carrinho
    return redirect(url_for('carrinho'))

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
    carrinho = session.get('carrinho', {})
    itens = []
    total = 0.0
    for id_str, qtd in carrinho.items():
        joia = next((j for j in joias if str(j['id']) == id_str), None)
        if joia:
            preco = float(joia['preco'].replace('R$', '').replace(',', '.'))
            subtotal = preco * qtd
            total += subtotal
            itens.append({
                'id': joia['id'],
                'nome': joia['nome'],
                'preco': joia['preco'],
                'qtd': qtd,
                'subtotal': f'R$ {subtotal:.2f}'.replace('.', ',')
            })
    return render_template('carrinho.html', itens=itens, total=f'R$ {total:.2f}'.replace('.', ','))

@app.route('/home')
def home():
    return render_template('home.html')

import os
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
