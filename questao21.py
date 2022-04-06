horas_trabalhadas = int(input("Informe o número de horas trabalhadas: "))
salario_minimo = float(input("Informe o valor do salário mínimo: "))
horas_extras = int(input("Informe o número de horas extras trabalhadas: "))

valor_hora_trabalho = salario_minimo * 1/8
valor_hora_extra = salario_minimo * 1/4

salario_bruto = horas_trabalhadas * valor_hora_trabalho
quantia_hora_extra = horas_extras * valor_hora_extra

salario_a_receber = salario_bruto + quantia_hora_extra

print("o salário a receber é %2.f" % salario_a_receber)