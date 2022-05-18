salario = float(input())

if salario <= 300:
    valor_aumento = salario + (salario * 0.5)
elif salario > 300 and salario <= 500:
    valor_aumento = salario + (salario * 0.4)
elif salario > 500 and salario <= 700:
    valor_aumento = salario + (salario * 0.3)
elif salario > 700 and salario <= 800:
    valor_aumento = salario + (salario * 0.2)
elif salario > 800 and salario <= 1000:
    valor_aumento = salario + (salario * 0.1)
else:
    valor_aumento = salario + (salario * 0.05)

print(f'O aumento será de {valor_aumento}')