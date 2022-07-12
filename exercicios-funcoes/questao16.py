vetor = []

for i in range(20):
    vetor.append(float(input()))

def somar_valores(vetor):
    soma = 0
    for i in range(len(vetor)):
        soma += vetor[i]
    return soma

somar_valores(vetor)