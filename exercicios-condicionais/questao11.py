salario = float(input())

if salario <= 300:
    aumento = salario * 0.15
    print(f'O novo salario é {salario + aumento}')
elif salario < 300 and salario < 600:
    aumento = salario * 0.10
    print(f'O novo salario é {salario + aumento}')
elif salario >=  600 and salario <= 900:
    aumento = salario * 0.05
    print(f'O novo salario é {salario + aumento}')
else:
    print(salario)