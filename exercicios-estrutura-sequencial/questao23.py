#Faça um programa que receba a medida de dois ângulos de um triângulo, calcule e mostre a medida do terceiro ângulo.

medida_angulo_x = int(input("Digite o valor do primeiro ângulo: "))
medida_angulo_y = int(input("Digite o valor do segundo ângulo: "))

medida_angulo_z = 180 - (medida_angulo_x + medida_angulo_y)

print("A medida do terceiro ângulo é %d" % medida_angulo_z)