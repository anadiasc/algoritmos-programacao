vetor = []
primos = []

for i in range(15):
    vetor.append(int(input()))

for j in range(len(vetor)):
    for k in range(len(vetor)-1):
        if vetor[j] == 2:
            primos.append(vetor[k])
        elif vetor[j] == vetor[k]:
            if vetor[j] % vetor[k+1] != 0:
                primos.append(vetor[k])
        elif vetor[j] != vetor[k]:
            if vetor[j] % vetor[k] != 0:
                primos.append(vetor[k])

print(primos)