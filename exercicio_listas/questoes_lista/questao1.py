lista = []
pares = []
impares = []

for i in range(6):
    lista.append(int(input()))
    if lista[i] % 2 == 0:
        pares.append(lista[i])
    else:
        impares.append(lista[i])

print(f'os numeros pares são {pares} e a quantidade é {len(pares)}')
print(f'os numeros impares são {impares} e a quantidade é {len(impares)}')

