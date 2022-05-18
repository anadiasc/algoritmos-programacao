codigo_produto = int(input())
qtd_comprada = int(input())


if codigo_produto >= 1 and codigo_produto <= 10:
    print('Preço unitário: 10')
    preco_total = 10 * qtd_comprada
    print(f'Preco total: {preco_total}')
elif codigo_produto >= 11 and codigo_produto<= 20:
    print('Preço unitário: 15')
    preco_total = 15 * qtd_comprada
    print(f'Preco total: {preco_total}')
elif codigo_produto >= 21 and codigo_produto <= 30:
    print('Preço unitário: 20')
    preco_total = 20 * qtd_comprada
    print(f'Preco total: {preco_total}')
elif codigo_produto >= 31 and codigo_produto <= 40:
    print('Preço unitário: 30')
    preco_total = 30 * qtd_comprada
    print(f'Preco total: {preco_total}')

if preco_total < 250:
    desconto = preco_total - (preco_total * 0.05)
    print(f'Preco total apos descontos: {desconto}')
elif preco_total >= 250 and preco_total <= 500:
    desconto = preco_total - (preco_total * 0.1)
    print(f'Preco total apos descontos: {desconto}')
else:
    desconto = preco_total - (preco_total * 0.15)
    print(f'Preco total apos descontos: {desconto}')