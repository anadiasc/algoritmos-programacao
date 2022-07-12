from calendar import c


def numerosPrimos():
    c = 100
    f = 150
    primos = []
    qtd = 0
    while qtd < 3:
        for i in range(c, f+1): 
            if i>1: 
                for j in range(2,i): 
                    if(i % j==0): 
                        break
                else: 
                     primos.append(i)
                     qtd += 1
    print(primos)
