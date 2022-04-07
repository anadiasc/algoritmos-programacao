# Faça um programa que receba o ano de nascimento de uma pessoa e o ano atual
ano_atual = int(input("Digite o ano atual: "))
ano_nascimento = int(input("Digite o seu ano de nascimento : "))

idade_anos = ano_atual - ano_nascimento
idade_meses = idade_anos * 12
idade_dias = idade_meses * 365
idade_semanas = idade_dias / 7

print("A idade em anos é {} \nA idade em meses é {} \nA idade em dias é {} \nA idade em semanas é {}".format(idade_anos, idade_meses, idade_dias, idade_semanas))