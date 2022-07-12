def calcular_media():
    soma = 0
    qtd_num = 0
    while True:
        entrada = int(input('digite um numero: '))
        soma += entrada
        qtd_num += 1
        if entrada == 0:
            qtd_num = qtd_num - 1
            break
    media = soma / qtd_num
    print(media)

calcular_media()