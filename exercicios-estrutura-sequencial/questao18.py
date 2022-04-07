#Faça um programa que receba uma temperatura em Celsius, calcule e mostre essa temperatura e Fahrenheit.

temperatura_celsius = int(input("Digite a temperatura em Celsius: "))

temperatura_fahrenheit = 180 * (temperatura_celsius + 32) / 100

print("A temperatura em fahrenheit é {}".format(temperatura_fahrenheit))