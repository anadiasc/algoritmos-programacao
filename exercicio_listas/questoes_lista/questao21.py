vetor1 = []
vetor2 = []

for i in range(2):
    vetor1.append(float(input()))

vetor2.append(vetor1)

for j in range(len(vetor1)):
    n = int(vetor2[j])
    m = vetor2[j] * 10
    s = n * 10

    if m != s:
        vetor2[j] = 1

print(vetor1, vetor2)
