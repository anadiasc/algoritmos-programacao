#ordem = f'{x}, {ordem}'
ordem = []

for i in range(1, 6):
    x = input()
    ordem += x
    if i == 5:
        print(ordem)
        print(sorted(ordem)) #ordem crescente
        ordem.sort(reverse=True) #ordem decrescente
        print(ordem)
for x in  ordem:
    print(x)