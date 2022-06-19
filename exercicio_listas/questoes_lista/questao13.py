nome = []
nota = []
soma = 0

for i in range(8):
    nome.append(input('nome: '))
    nota.append(float(input('nota: ')))
    soma += nota[i]

media = soma / len(nota)

print('RELATORIO DE NOTAS:')
for j in range(len(nome)):
    print(nome[j],'',nota[j])
print(f'media da classe = {media}')
