while True:
    print('Menu de opções:\n1. Média aritmética\n2. Média ponderada\n3. sair')

    escolha = int(input('Digite a opção desejada: '))

    if escolha == 1:
        n1=float(input())
        n2=float(input())
        media = (n1 + n2) / 2
        print(media)
    elif escolha == 2:
        n1=float(input())
        n2=float(input())
        n3=float(input())

        p1=float(input())
        p2=float(input())
        p3=float(input())

        soma_peso = p1 + p2 + p3
        media_pond = (n1 * p1) + (n2 * p2) + (n3 * p3)
        print(media_pond)
    else:
        break