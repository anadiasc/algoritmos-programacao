idade = int(input())
peso = float(input())

if idade < 20:
    if peso < 60:
        print(9)
    elif peso >= 60 and peso <= 90:
        print(6)
    elif peso > 90:
        print(3)
elif idade >= 20 and idade <= 50:
    if peso < 60:
        print(8)
    elif peso >= 60 and peso <= 90:
        print(5)
    elif peso > 90:
        print(2)
else:
    if peso < 60:
        print(7)
    elif peso >= 60 and peso <= 90:
        print(4)
    elif peso > 90:
        print(1)