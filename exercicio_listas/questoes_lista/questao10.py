vetor1 = []
vetor2 = []
vetor1R = [] #sera composto pela soma de cada numero par do primeiro vetor somado a todos os numeros do segundo vetor 
vetor2R = [] #sera composto pela quantidade de divisores que cada numero impar do primeiro vetor tem no segundo vetor
somav2 = 0
divisores = 0

for i in range(10):
    vetor1.append(int(input('digite um numero para o primeiro vetor: ')))

for j in range(5):
    vetor2.append(int(input('digite um numero para o segundo vetor: ')))
    somav2 += vetor2[j]

for k in range(len(vetor1)):
    if vetor1[k] % 2 == 0:
        aux = vetor1[k] + somav2
        vetor1R.append(aux)

for l in range(len(vetor1)):
    if vetor1[l] % 2 != 0:
        for m in range(len(vetor2)):
            if vetor1[l] % vetor2[m] == 0:
                divisores += 1
        vetor2.append(divisores)

print(f'Primeiro vetor resultante: {vetor1R}\nSegundo vetor resultante: {vetor2R}')