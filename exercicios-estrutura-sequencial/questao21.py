#Faça um programa que receba o número de horas trabalhadas, o valor do salário mínimo e o número de horas extras trabalhadas, calcule e mostre o salário a receber, de acordo com as regras a seguir: a) a hora trabalhada vale 1/8 do salário mínimo; b) a hora extra vale 1/4 do salário mínimo;c) o salário bruto equivale ao número de horas trabalhadas multiplicado pelo valor da hora trabalhada; d) a quantia a receber pelas horas extras equivale ao número de horas extras trabalhadas multiplicado pelo valor da hora extra; e) o salário a receber equivale ao salário bruto mais a quantia a receber pelas horas extras.

horas_trabalhadas = int(input("Informe o número de horas trabalhadas: "))
salario_minimo = float(input("Informe o valor do salário mínimo: "))
horas_extras = int(input("Informe o número de horas extras trabalhadas: "))

valor_hora_trabalho = salario_minimo * 1/8
valor_hora_extra = salario_minimo * 1/4

salario_bruto = horas_trabalhadas * valor_hora_trabalho
quantia_hora_extra = horas_extras * valor_hora_extra
salario_a_receber = salario_bruto + quantia_hora_extra

print("o salário a receber é %2.f" % salario_a_receber)