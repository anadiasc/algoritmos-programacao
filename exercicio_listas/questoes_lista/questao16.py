produto = []
preco = []
nome_50_100 = []
menor_50 = soma_100 = 0
qtd_mais100 = 1

for i in range(5):
    produto.append(input('insira o produto: '))
    preco.append(float(input('insira o preco: ')))

for j in range(len(produto)):
    if preco[j] < 50:
        menor_50 += 1
    elif preco[j] >= 50 and preco <= 100:
        nome_50_100.append(produto[j])
    else:
        soma_100 += preco[j]
        qtd_mais100 += 1

print(f'Quantidade de produtos com preco inferior a R$ 50,00: {menor_50}')
print(f'Nome dos produtos com preco entre R$ 50,00 e R$ 100,00: {nome_50_100}')
print(f'Média dos precos acima de R$ 100,00: {soma_100 / qtd_mais100}')
