vetor = []
maior = 0

for i in range(2):
    vetor.append(int(input()))

for j in range(len(vetor)):
    if j == 0:
        maior = vetor[j]
    elif maior < vetor[j]:
        maior = vetor[j]

for k in range(len(vetor)):
    aux = vetor[k] / maior
    vetor[k] = aux

print(vetor)