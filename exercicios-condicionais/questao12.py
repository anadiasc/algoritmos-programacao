salario_bruto = float(input())
imposto = 0.07

if salario_bruto <= 350:
    print(f'O salario atual é {(salario_bruto - (salario_bruto * imposto)) + 100}')
elif salario_bruto > 350 and salario_bruto < 600:
    print(f'O salario atual é {(salario_bruto - (salario_bruto * imposto)) + 75}')
elif salario_bruto >= 600 and salario_bruto <= 900:
    print(f'O salario atual é {(salario_bruto - (salario_bruto * imposto)) + 50}')
else:
    print(f'O salario atual é {(salario_bruto - (salario_bruto * imposto)) + 35}')