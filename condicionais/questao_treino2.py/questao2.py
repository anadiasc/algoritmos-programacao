nota1 = float(input())
nota2 = float(input())

media = (nota1 + nota2) / 2

if media >= 7:
    print("Aprovado")
elif media < 7 and media >= 3:
    print("Exame")
else:
    print("Reprovado")
