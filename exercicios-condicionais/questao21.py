codigo_produto = int(input())

if codigo_produto == 1:
    print('Pocedência: Sul')
elif codigo_produto == 2:
    print('Pocedência: Norte')
elif codigo_produto == 3:
    print('Pocedência: Leste')
elif codigo_produto == 4:
    print('Pocedência: Oeste')
elif codigo_produto == 5 or codigo_produto == 6:
    print('Nordeste')
elif codigo_produto >=7 and codigo_produto <= 9:
    print('Pocedência: Sudeste')
elif codigo_produto >= 10 and codigo_produto <= 20:
    print('Pocedência: Centro-Oeste')
elif codigo_produto >= 21 and codigo_produto <= 30:
    print('Pocedência: Nordeste')
    
