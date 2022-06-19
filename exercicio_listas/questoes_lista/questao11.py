vetor = []
vetor1 = []
vetor2 = []

for i in range(10):
    vetor.append(int(input()))

for j in range(len(vetor)):
    if vetor[j] % 2 == 0:
        vetor1.append(vetor[j])
    else:
        vetor2.append(vetor[j])

print(f'vetor par {vetor1}\nvetor impar{vetor2}')