lista = []
negativos = positivos = 0

for i in range(10):
    lista.append(float(input()))

for j in range(len(lista)):
    if lista[j] < 0:
        negativos += 1
    else:
        positivos += lista[j]

print(negativos, positivos)
