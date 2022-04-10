num1 = int(input())
num2 = int(input())

print("Menu de opções: \n 1. Média entre os numeros \n 2. Diferença do maior pelo menor \n 3. Produto entre os numeros digitados \n 4. divisão do primeiro pelo segundo")

escolha = int(input("Digite a opção desejada: "))

if escolha == 1:
    media = (num1 + num2) / 2
    print(f'A média é {media}')
elif escolha == 2:
    if num1 > num2:
        print(num1 - num2)
    else:
        print(num2 - num1)
elif escolha == 3:
   print(num1 * num2)
elif escolha == 4:
     if num2 != 0:
        print(num1 / num2)
else:
    print("Escolha inválida")