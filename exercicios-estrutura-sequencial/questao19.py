# Sabe-se que, para iluminar de maneira correta os cômodos de uma casa, para cada m2, deve-se usar 18 Wde potência. Faça um programa que receba as duas dimensões de um cômodo (em metros), calcule e mostre a sua área (em m2) e a potência de iluminação que deverá ser utilizada.
largura = float(input("Informe a largura em metros: "))
comprimento = float(input("Informe o comprimento em metros: "))

area = largura * comprimento
potencia_iluminacao = area * 18

print("A área do cômodo é {} \nA potência de iluminação que deverá ser utilizada é {}".format(area, potencia_iluminacao))