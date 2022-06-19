vetor = []
maior = []
menor = []

for i in range(15):
    vetor.append(int(input('digite um numero: ')))

for j in range(len(vetor)):
    if j == 0:
        maior.append(f'O maior é {vetor[j]} no index {j}')
    elif maior[j] < vetor[j]:
        maior.append(f'O maior é {vetor[j]} no index {j}')

for k in range(len(vetor)):
    if k == 0:
        menor.append(f'O menor é {vetor[k]} no index {k}')
    elif menor[k] < vetor[k]:
        menor.append(f'O menor é {vetor[k]} no index {k}')

print(maior, menor)
