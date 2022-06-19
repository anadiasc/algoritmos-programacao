codigo = []
estoque = []
pedidos = []

for i in range(10):
    codigo.append(int(input('para cadastrar um novo produto, digite o codigo: ')))
    estoque.append(int(input('agora, digite a quantidade em estoque: ')))

while True:
    cliente = int(input('insira o codigo do cliente: '))
    if cliente == 0:
        break
    produto = int(input('insira o codigo do produto: '))
    quantidade = int(input('insira a quantidade desejada: '))
#verifica se o produto e a quantidade são compativeis com a demanda
    if produto not in codigo:
        print('codigo inexistente')
    else:
        for i in range(len(codigo)):
            if produto == codigo[i]:
                if quantidade <= estoque[i] and quantidade != 0:
                    pedidos.append(f'O cliente {cliente} solicita o produto {produto} com a seguinte quantidade {quantidade}')
                    print('Pedido atendido! Obrigado, volte sempre.')
                    estoque[i] = estoque[i] - quantidade
                else:
                    print('não possuimos estoque suficiente')

print('Etoque atualizado:')
for y in range(len(codigo)):
    print(f'codigo do produto {codigo[y]}| quantidade {estoque[y]}')