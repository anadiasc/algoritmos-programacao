preco = float(input())
categoria = int(input('Informe \n1. Limpeza\n2. Alimentaçãon\n3. Vestuário: '))
situacao = str(input('Informe R ou N: '))

if (preco <= 25):
    if (categoria == 1):
        novo_preco = preco + (preco * 0.05)
    elif (categoria == 2):
        novo_preco = preco + (preco * 0.08)
    elif (categoria == 3):
        novo_preco = preco + (preco * 0.1)
else:
    if (categoria == 1):
        novo_preco = preco + (preco * 0.12)
    elif (categoria == 2):
        novo_preco = preco + (preco * 0.15)
    elif (categoria == 3):
        novo_preco = preco + (preco * 0.18)

if (categoria == 2 or situacao == 'R'):
    preco_final = novo_preco - (novo_preco * 0.05)
else:
    preco_final = novo_preco - (novo_preco * 0.08)

if (preco_final <= 50):
    classificacao = 'barato'
elif (preco_final > 50 and preco_final < 120):
    classificacao = 'normal'
else:
    classificacao = 'caro'

print(novo_preco , preco_final, classificacao)