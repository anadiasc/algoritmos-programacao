def triangulo(lado1, lado2, lado3):
    if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
        print('forma um triangulo')
        if lado1 == lado2 and lado1 == lado3:
            print('triangulo equilatero')
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            print('triangulo isosceles')
        else:
            print('triangulo escaleno')
    else:
        print('não forma um triangulo')
