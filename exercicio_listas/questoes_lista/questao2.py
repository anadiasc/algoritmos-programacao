lista = []
multi_2_3 = []
multi_2 = []
multi_3 = []

for i in range(6):
    lista.append(int(input()))
    if lista[i] % 2 == 0 and lista[i] % 3 == 0:
        multi_2_3.append(lista[i])
    elif lista[i] % 2 == 0:
        multi_2.append(lista[i])
    elif lista[i] % 3 == 0:
        multi_3.append(lista[i])

print(f'os numeros multiplos de 2 são {multi_2}\nos numeros multiplos de 3 são {multi_3}\nos numeros multiplos de 2 e 3 são {multi_2_3}')
