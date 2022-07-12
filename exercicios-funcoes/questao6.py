def calcular_imc(alt):
    genero = input('qual o seu genero?[M/F] ')
    
    if 'M' in genero or 'm' in genero:
        peso_ideal = 72.7 * alt - 58
        print(peso_ideal)
    elif 'f' in genero or 'F' in genero:
        peso_ideal = 62.1 * alt - 44.7
        print(peso_ideal)
