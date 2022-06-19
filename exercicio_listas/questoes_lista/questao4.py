inteiros = []
iguais_30 = []

for i in range(15):
    inteiros.append(int(input()))

for y in range(len(inteiros)):
    if inteiros[y] == 30:
        iguais_30.append(f'index {y}')

print(iguais_30)