vetor = []

for i in range(15):
    vetor.append(int(input()))

def qtd_pares(vetor):
    qtd = 0
    for i in range(len(vetor)):
        if vetor[i] % 2 == 0:
            qtd += 1
    print(f'quantidade de valores pares: {qtd}')

qtd_pares(vetor)