salario_medio = float(input())

if salario_medio >= 200:
    credito = salario_medio * 0.10
    print(f'O credito concedido é de {credito}')
elif salario_medio > 200 and salario_medio <= 300:
    credito = salario_medio * 0.20
    print(f'O credito concedido é de {credito}')
elif salario_medio > 300 and salario_medio <= 400:
    credito = salario_medio * 0.25
    print(f'O credito concedido é de {credito}')
else:
    credito = salario_medio * 0.40
    print(f'O credito concedido é de {credito}')