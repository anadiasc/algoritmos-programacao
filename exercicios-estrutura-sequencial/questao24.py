#Faça um programa que receba a quantidade de dinheiro em reais que uma pessoa que vai viajar possui. Ela vai passar por vários países e precisa converter seu dinheiro em dólares, marco alemão e libra esterlina. Sabe-se que a cotação do dólar é de R$ 1,80; do marco alemão, de R$ 2,00; e da libra esterlina, de R$ 3,57. O programa deve fazer as conversões e mostrá-las

dinheiro_reais = float(input("Quantidade de dinheiro em reais: "))
dolar = 1.80
marco_alemao = 2
libra_esterlina = 3.57

dinheiro_dolar = dinheiro_reais / dolar
dinheiro_alemao = dinheiro_reais / marco_alemao
dinheiro_libra = dinheiro_reais / libra_esterlina

print("A quantidade de dinheiro em dólar é %2.f \nA quantidade de dinheiro em marco alemão é %2.f \nA quantidade de dinheiro em libra esterlina é %2.f" % (dinheiro_dolar, dinheiro_alemao, dinheiro_libra))