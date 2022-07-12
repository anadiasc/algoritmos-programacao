a = []
b = []

for i in range(3):
    a.append(int(input()))
    b.append(int(input()))

def intersecção(vetor1, vetor2):
    numeros_comuns = []
    for i in range(len(vetor1)):
        for j in range(len(vetor2)):
            if vetor1[i] == vetor2[j]:
                numeros_comuns.append(vetor1[i])
    print(numeros_comuns)

intersecção(a, b)