'''
5 => 120 vendidos | despesas 200(valor fixo)
-0,5 => +26 vendidos
obs: o preco deve estar entre 5 e 1 variando sempre em 0,5

saida:
lucro maximo
preco ingresso
quant vendida
valor = 5
for i in range(9, 1, -1):
    valor -= 0.5
    print(valor)
''' 
despesas = 200
valor = 5
for i in range(9, 1, -1):
    valor -= 0.5
    if valor == 4.5:
        qtd_vendida = 120 + 26
        faturamento = valor * qtd_vendida
        lucro = faturamento - despesas
        print(lucro, qtd_vendida, valor)
    elif valor == 4:
        qtd_vendida = 120 + 26*2
        faturamento = valor * qtd_vendida
        lucro = faturamento - despesas
        print(lucro, qtd_vendida, valor)
    elif valor == 3.5:
        qtd_vendida = 120 + 26*3
        faturamento = valor * qtd_vendida
        lucro = faturamento - despesas
        print(lucro, qtd_vendida, valor)
    elif valor == 3:
        qtd_vendida = 120 + 26*4
        faturamento = valor * qtd_vendida
        lucro = faturamento - despesas
        print(lucro, qtd_vendida, valor)
    elif valor == 2.5:
        qtd_vendida = 120 + 26*5
        faturamento = valor * qtd_vendida
        lucro = faturamento - despesas
        print(lucro, qtd_vendida, valor)
    elif valor == 2:
        qtd_vendida = 120 + 26*6
        faturamento = valor * qtd_vendida
        lucro = faturamento - despesas
        print(lucro, qtd_vendida, valor)
    elif valor == 1.5:
        qtd_vendida = 120 + 26*7
        faturamento = valor * qtd_vendida
        lucro = faturamento - despesas
        print(lucro, qtd_vendida, valor)
    elif valor == 1:
        qtd_vendida = 120 + 26*8
        faturamento = valor * qtd_vendida
        lucro = faturamento - despesas
        print(lucro, qtd_vendida, valor)
