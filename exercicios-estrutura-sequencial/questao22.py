#Faça um programa que receba o número de lados de um polígono convexo, calcule e mostre o número de diagonais desse polígono. Sabe-se que ND = N * (N − 3)/2, em que N é o número de lados do polígono.

num_lados = int(input("Informe o número de lados de um polígono convexo: "))
num_diagonais = num_lados * (num_lados - 3) / 2

print("O número de diagonais desse polígono é %2.f" % num_diagonais)