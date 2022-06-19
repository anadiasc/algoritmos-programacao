tabuleiro = [1, 2, 3, 4, 5, 6, 7, 8, 9]
quadrado_magico = [4, 9, 2, 3, 5, 7, 8, 1, 6] #ajuda a verificar se o jogador ganhou o jogo

#mostrar tabuleiro
def mostrar_tabuleiro():
    print(tabuleiro[0], '|', tabuleiro[1], '|', tabuleiro[2])
    print('--|---|--')
    print(tabuleiro[3], '|', tabuleiro[4], '|', tabuleiro[5])
    print('--|---|--')
    print(tabuleiro[6], '|', tabuleiro[7], '|', tabuleiro[8])
    print()
#checar vitoria
def checar_vitoria(jogador):
    for x in range(9):
        for y in range(9):
            for z in range(9):
                if x != y and y != z and z != x:
                    if tabuleiro[x] == jogador and tabuleiro[y] == jogador and tabuleiro[z] == jogador:
                        if quadrado_magico[x] + quadrado_magico[y] + quadrado_magico[z] == 15:
                            print("Jogador", jogador ,"ganhou!\n")
                            return True
#Aplicando o jogo da velha sempre começando com o jogador 'X'
while True:
    mostrar_tabuleiro()
    numero = int(input('Jogador X escolha um espaço: ')) - 1

    for i in range(9):
        if numero == i:
            tabuleiro[i] = 'X'
            mostrar_tabuleiro()

    venceu = checar_vitoria('X') 
    if venceu == True:
        break
    else:
        numero = int(input('Jogador O escolha um espaço: ')) - 1
    
    for i in range(9):
        if numero == i:
            tabuleiro[i] = 'O'
            mostrar_tabuleiro()
            
    venceu = checar_vitoria('O')
    if venceu == True:
        break