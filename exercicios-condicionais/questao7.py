salario = float(input())

if salario < 500:
    aumento = salario * 0.30
    print(f'O novo salário é {salario + aumento}')
else:
    print('Infelizmente, fora da público alvo do aumento')