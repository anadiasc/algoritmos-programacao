largura = float(input("Informe a largura em metros: "))
comprimento = float(input("Informe o comprimento em metros: "))

area = largura * comprimento
potencia_iluminacao = area * 18

print("A área do cômodo é {} \nA potência de iluminação que deverá ser utilizada é {}".format(area, potencia_iluminacao))