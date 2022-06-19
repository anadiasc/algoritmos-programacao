vetor1 = []
vetor2 = []
vetor_resultante = []

for i in range(2):
    vetor1.append(int(input('digite um numero para o 1º vetor: ')))
    vetor_resultante.append(vetor1[i])

for j in range(2):
    vetor2.append(int(input('digite um numero para o 2º vetor: ')))
    vetor_resultante.append(vetor2[j])

for k in range(len(vetor_resultante)):
    for l in range(len(vetor_resultante)-1):
        if vetor_resultante[l] < vetor_resultante[l + 1]:
            aux = vetor_resultante[l]
            vetor_resultante[l] = vetor_resultante[l + 1]
            vetor_resultante[l + 1] = aux

print(vetor_resultante)