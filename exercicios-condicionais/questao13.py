preco_produto = float(input())

def classificacao(novo_preco):
    if novo_preco < 80:
        print('Classificação: Barato')
    elif novo_preco >= 80 and novo_preco <= 120:
        print('Classificação: Normal')
    elif novo_preco >= 120 and novo_preco <= 200:
        print('Classificação: Caro')
    else:
        print('Classificação: Muito Caro')

if preco_produto < 50:
    novo_preco = preco_produto + (preco_produto * 0.05)
    print(f'O novo preco é {novo_preco}')
    classificacao(novo_preco)
elif preco_produto >= 50 and preco_produto <= 100:
    novo_preco = preco_produto + (preco_produto * 0.1)
    print(f'O novo preco é {novo_preco}')
    classificacao(novo_preco)
else:
    novo_preco = preco_produto + (preco_produto * 0.15)
    print(f'O novo preco é {novo_preco}')
    classificacao(novo_preco)