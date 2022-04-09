num1 = int(input())
num2 = int(input())

print("Menu de opções: \n 1. O primeiro numero elevado pelo segundo \n 2. Raiz quadrada de cada um dos numeros \n 3. Raiz cubica de cada um dos numeros")

escolha = int(input("Digite a opção desejada: "))

if escolha == 1:
    print(num1 ** num2)
elif escolha == 2:
    print(num1 ** 0.5)
    print(num2 ** 0.5)
elif escolha == 3:
    print(num1 ** (1/3))
    print(num2 ** (1/3))
else:
    print("Opção inválida")