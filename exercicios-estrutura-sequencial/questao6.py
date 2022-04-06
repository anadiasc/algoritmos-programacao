# Um funcionário recebe um salário fixo mais 4% de comissão sobre as vendas. Faça um programa que receba o salário fixo do funcionário e o valor de suas vendas, calcule e mostre a comissão e seu salário final.

salario_fixo = float(input("Digite o salario fixo: "))
valor_venda = float(input("Digite o valor de vendas: "))

comissao = valor_venda * 0.04
salario_final = salario_fixo + comissao
print(comissao)
print(salario_final)