custo_fabrica = float(input())

if custo_fabrica < 12000:
    preco_consumidor = (custo_fabrica * 0.05) + custo_fabrica
    print(preco_consumidor)
elif custo_fabrica >= 12000 and custo_fabrica <= 25000:
    preco_consumidor = custo_fabrica + (custo_fabrica * 0.1) + (custo_fabrica * 0.15)
    print(preco_consumidor)
else:
    preco_consumidor = custo_fabrica + (custo_fabrica * 0.15) + (custo_fabrica * 0.2)
    print(preco_consumidor)