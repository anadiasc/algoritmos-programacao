idade = []
sexo = []
salario = []
num_filhos = []

for i in range(15):
    idade.append(int(input('informe a idade: ')))
    sexo.append(input('informe o sexo:[M/F] '))
    salario.append(int(input('informe o salario: ')))
    num_filhos.append(int(input('informe o nº de filhos: ')))

def calcular_mediaSalarial(salario):
    soma = 0
    for i in range(len(salario)):
        soma += salario[i]
    media = soma / len(salario)
    print(f'A media salarial entre os habitantes é: {media:.2f}')

def calcular_maiorIdade(idade):
    maior = 0
    for i in range(len(idade)):
        if idade[i] > maior:
            maior = idade[i]
        elif maior < idade[i]:
            maior = idade[i]
    print(f'maior idade é: {maior}')

def calcular_menorIdade(idade):
    menor = 0
    for i in range(len(idade)):
        if i == 0:
            menor = idade[i]
        elif idade[i] < menor:
            menor = idade[i]
    print(f'menor idade é: {menor}')

def mostrar_grupoMulheres(sexo, salario, filhos):
    qtd = 0
    for i in range(len(sexo)):
        if 'f' in sexo[i] or 'F' in sexo[i]:
            if salario[i] <= 500:
                if filhos[i] == 3:
                    qtd += 1
    print(f'A quantidade de milheres que tem tres filhos e recebem até R$ 500,00 reais é: {qtd}')
