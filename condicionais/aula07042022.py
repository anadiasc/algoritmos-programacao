'''
Condicionais:
if, else, elif -> se a exepressão dada for verdadeira, será execuatado o comando dentro da estrutura
while
for -> utilizado para laços de repetição
'''
#Exemplo if:
x = 20
y = 10
if x >=10 and y >=2:
    print('Estamos dentro da estrutura IF 1')
#Exemplo if, else:
idade = int(input('digite sua idade: '))
if idade >= 18:
    print('já pode tirar sua habilitação')
else:
    qnt = 18 - idade
    print('espere mais', qnt, ' ano(s)')