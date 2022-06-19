vetor = []
soma = 0
for i in range(5):
    vetor.append(int(input(f'digte o {i+1}º numero: ')))
    soma += vetor[i]

for j in range(1):
    print(f'Os numeros digitados foram: {vetor[j]} + {vetor[j+1]} + {vetor[j+2]} + {vetor[j+3]} + {vetor[j+4]} = {soma}')

