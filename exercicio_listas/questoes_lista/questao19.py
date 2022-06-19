vetor1 = []
vetor2 = []
vetor_resultante = []

for i in range(10):
    vetor1.append(int(input()))
for i in range(10):
    vetor2.append(int(input()))

for j in range(len(vetor1)):
    aux = vetor1[j] * vetor2[j]
    vetor_resultante.append(aux)

print(vetor_resultante)