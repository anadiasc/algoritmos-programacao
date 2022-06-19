logica = []
programacao = []
iguais = []

while True:
    for i in range(15):
        logica.append(int(input()))
    for j in range(10):
        programacao.append(int(input()))

    for k in range(len(logica)):
        for l in range(len(logica)-1):
            if logica[k] == programacao[l]:
                iguais.append(logica[k])
    
    print(len(iguais))
    break