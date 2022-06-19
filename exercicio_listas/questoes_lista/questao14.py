aluno = []
nota1 = []
nota2 = []
medias = []
aprovados = []
reprovados = []
exame = 0
soma_classe = 0
media_classe = 0

for i in range(2):
    aluno.append(input('Aluno: '))
    nota1.append(float(input('1º nota: ')))
    nota2.append(float(input('2º nota: ')))

for j in range(len(medias)):
    media = float((nota1[j] + nota2[j]) / 2)

    medias.append(media)

    soma_classe += media[j]

    if media[j] >= 7:
        aprovados.append(aluno[j])
    elif media[j] > 3 and media[j] < 7:
        exame += 1
    else:
        reprovados.append(aluno[j])

media_classe = soma_classe / 6

for l in range(7):
    for k in range(12):
        if aluno[k] == aprovados[k]:
            print(f'Aluno: {aluno[k]}\n1º nota:  {nota1[k]}\n2º nota: {nota2[k]}\nMédia: {medias[k]}\nSituação: Aprovado\n')
        elif aluno[k] == reprovados[k]:
            print(f'Aluno: {aluno[k]}\n1º nota:  {nota1[k]}\n2º nota: {nota2[k]}\nMédia: {medias[k]}\nSituação: Reprovado\n')

print(f'Média da classe: {media_classe}')
print(f'Percentual de alunos aprovados: {(len(aprovados) * 100) / 6}')
print(f'Percentual de alunos de exame: {(exame * 100) / 6}')
print(f'Percentual de alunos reprovados: {(len(reprovados) * 100) / 6}')
