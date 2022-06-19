vetor = []
positivo = []

for i in range(2):
    vetor.append(int(input()))

for j in range(len(vetor)):
    if vetor[j] % 2 == 0:
        positivo.append(vetor[j])

print(positivo)
