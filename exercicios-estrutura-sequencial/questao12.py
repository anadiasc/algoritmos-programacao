#Faça um programa que receba o valor do salário mínimo e o valor do salário de um funcionário, calcule e mostre a quantidade de salários mínimos que esse funcionário ganha.
salario_minimo = float(input("Digite o valor do salario mínimo: "))
salario_funcionario = float(input("Digite o salario do funcionário: "))

quantidade_de_salario_recebido = salario_funcionario / salario_minimo

print(f"A quantidade de salarios mínimos recebidos pelo funcionário é {quantidade_de_salario_recebido}")