aluno = []
nota = []
maior = 0

for i in range(3):
    aluno.append(input())
    nota.append(float(input()))

for j in range(len(aluno)):
    if nota[j] >= maior:
        maior = nota[j]
    elif maior < nota[j]:
        maior = nota[j]

    if nota[j] < 7:
        esperado = 14 - nota[j]
        print('{aluno[j]}, você precisa tirar {esperado} para ter êxito na prova final')
        
