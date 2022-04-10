salario = float(input())

def valor_aumento(aumento):
    valor_aumento = salario + (salario * aumento)
    print(f'O aumento será de {valor_aumento}')

if salario <= 300:
    valor_aumento(0.5)
elif salario > 300 and salario <= 500:
    valor_aumento(0.4)
elif salario > 500 and salario <= 700:
    valor_aumento(0.3)
elif salario > 700 and salario <= 800:
    valor_aumento(0.2)
elif salario > 800 and salario <= 1000:
    valor_aumento(0.1)
else:
    valor_aumento(0.5)