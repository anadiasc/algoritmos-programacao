preco = float(input())

if (preco < 30):
    print(f'Não tem desconto\nO preco é {preco}')
elif (preco >= 30 and preco <= 100):
    print(f'O desconto é {preco - (preco * 0.1)}\nO preco é {preco}')
else:
    print(f'O desconto é {preco - (preco * 0.15)}\nO preco é {preco}')