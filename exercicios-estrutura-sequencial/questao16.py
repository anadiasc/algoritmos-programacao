# Faça um programa que receba o valor dos catetos de um triângulo, calcule e mostre o valor da hipotenusa.

cateto_oposto = int(input("Digite o valor do cateto oposto: "))
cateto_adjacente = int(input("Digite o valor do cateto adjacente: "))

hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)

print("O valor da hipotenusa é %2.f" % hipotenusa)
