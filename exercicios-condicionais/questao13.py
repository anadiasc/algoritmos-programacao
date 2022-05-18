preco_produto = float(input())

if preco_produto < 50:
    novo_preco = preco_produto + (preco_produto * 0.05)
elif preco_produto >= 50 and preco_produto <= 100:
    novo_preco = preco_produto + (preco_produto * 0.1)
else:
    novo_preco = preco_produto + (preco_produto * 0.15)

if novo_preco < 80:
    classificacao = 'Barato'
elif novo_preco >= 80 and novo_preco <= 120:
    classificacao = 'Normal'
elif novo_preco >= 120 and novo_preco <= 200:
    classificacao = 'Caro'
else:
    classificacao = 'Muito caro'

print(f'O novo preco é {novo_preco}')
print(classificacao)