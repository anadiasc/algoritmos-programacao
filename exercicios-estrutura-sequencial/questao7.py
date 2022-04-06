#Faça um programa que receba o peso de uma pessoa, calcule e mostre:
#a) o novo peso, se a pessoa engordar 15% sobre o peso digitado;
#b) o novo peso, se a pessoa emagrecer 20% sobre o peso digitado.

peso = float(input("Digite peso: "))

peso_15 = (peso * 0.15) + peso
peso_20 = peso - (peso * 0.20)

print(peso_15)
print(peso_20)