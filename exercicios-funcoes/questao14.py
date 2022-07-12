x = []

for i in range(30):
    x.append(int(input('digite valores inteiros: ')))

def separar_positivoNegativo(lista):
    a = []
    b = []
    for i in range(len(lista)):
        if lista[i] > 0:
            a.append(lista[i])
        else:
            b.append(lista[i])
    return a, b
