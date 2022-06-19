nome_vendedor = []
percentual = []
vendas = []
comissao = []
maior = menor = total_vendas = 0
nome_maior = ''
nome_menor = ''

for i in range(10):
    nome_vendedor.append(input('Nome do vendedor: '))
    percentual.append(float(input('Porcentagem da comissão: ')) / 100)
    vendas.append(float(input('Vendas feitas (em reais): ')))

    comissao.append(percentual[i] * vendas[i])

print('Relatório de Vendas:\nVendedor|Valor a receber')
for j in range(len(nome_vendedor)):
    print(f'{nome_vendedor[j]}|{comissao[j]}')

for k in range(len(nome_vendedor)):
    if k == 0:
        maior = comissao[0]
        nome_maior = nome_vendedor[k]
    elif maior < comissao[k]:
        maior = comissao[k]
        nome_maior = nome_vendedor[k]

print(f'O vendedor {nome_maior} receberá o maior valor que é {maior}')

for l in range(len(nome_vendedor)):
    if l == 0:
        menor = comissao[0]
        nome_menor = nome_vendedor[l]
    elif menor > comissao[l]:
        menor = comissao[l]
        nome_menor = nome_vendedor[l]

print(f'O vendedor {nome_menor} receberá o menor valor que é {menor}')