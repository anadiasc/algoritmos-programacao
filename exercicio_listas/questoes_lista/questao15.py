cliente = []
qtd_2011 = []
gratis = []

for i in range(8):
    cliente.append(input('cliente: '))
    qtd_2011.append(int(input('quantidades locadas em 2011: ')))

for j in range(len(cliente)):
    qtd_gratis = qtd_2011[j] // 10
    gratis.append(qtd_gratis)

print('--------Base Clientes 2011--------')
for k in range(len(cliente)):
    print(f'Cliente: {cliente[k]}\nLocações grátis: {gratis[k]}\n')
