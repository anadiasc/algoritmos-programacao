print('Menu de investimentos:\n 1.Poupança\n 2.Fundos de renda fixa')

tipo_investimento = int(input('Informe o tipo de investimento: '))
valor_investimento = float(input('Informe o valor do investimento: '))

if tipo_investimento == 1:
    rendimento = valor_investimento + (valor_investimento * 0.03)
    print(rendimento)
elif tipo_investimento == 2:
    rendimento = valor_investimento + (valor_investimento * 0.04)
    print(rendimento)
