salario_joao = float(input("Digite seu salario: "))
conta1 = float(input("Digite o valor da primeira conta: "))
conta2 = float(input("Digite o valor da segunda conta: "))
multa = 0.02

salario_restante = salario_joao - ((conta1 * multa + conta1) + (conta2 * multa + conta2))

print("O salario restante de João é %.2f" % salario_restante)