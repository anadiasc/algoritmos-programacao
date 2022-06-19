produto = []
codigo = []
valor = []

for i in range(3):
    produto.append(input('insira nome do produto: '))
    codigo.append(int(input('insira codigo do produto: ')))
    valor.append(float(input('insira valor do produto: ')))

for j in range(len(produto)):
    if codigo[j] % 2 == 0 and valor[j] > 1000:
        novo = valor[j] + (valor[j] * 0.2)
        valor.append(novo)
    elif codigo[j] % 2 == 0:
        novo = valor[j] + (valor[j] * 0.15)
        valor.append(novo)
    elif valor[j] > 1000:
        novo = valor[j] + (valor[j] * 0.1)
        valor.append(novo)

print()
print('---------------RELATÓRIO---------------')
print()
for k in range(len(produto)):
    print(f'PRODUTO | {produto[k]}\nCODIGO  | {codigo[k]}\nPRECO   | {valor[k]}\n')