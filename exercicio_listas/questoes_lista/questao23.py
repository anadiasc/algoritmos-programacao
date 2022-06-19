a = []
b = []
acumulado = 0

for i in range(5):
    a.append(int(input()))
    b.append(int(input()))

for j in range(len(a)):
    if j == 0:
        aux = a[j] - b[j + 4]
        acumulado += aux
    elif j == 1:
        aux = a[j] - b[j + 3]
        acumulado += aux
    elif j == 2:
        aux = a[j] - b[j + 2]
        acumulado += aux
    elif j == 3:
        aux = a[j] - b[j + 1]
        acumulado += aux
    elif j == 4:
        aux = a[j] - b[j + 0]
        acumulado += aux

print(acumulado)
