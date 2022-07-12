meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
temperatura = []

for i in range(12):
    temperatura.append(float(input(f'Insira a temperatura do {i+1}º mês: ')))

def maior_temperatura(temperatura):
    maior = 0
    mes = ''
    for i in range(len(temperatura)):
        if i == 0:
            maior = temperatura[i]
            mes = meses[i]
        elif maior < temperatura[i]:
            maior = temperatura[i]
            mes = meses[i]
    print(f'A maior temperatura foi {maior} no mes {mes}')

def menor_temperatura(temperatura):
    menor = 0
    mes = ''
    for i in range(len(temperatura)):
        if i == 0:
            menor = temperatura[i]
            mes = meses[i]
        elif menor > temperatura[i]:
            menor = temperatura[i]
            mes = meses[i]
    print(f'A maior temperatura foi {menor} no mes {mes}')

maior_temperatura(temperatura)
menor_temperatura(temperatura)