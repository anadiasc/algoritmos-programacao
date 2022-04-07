#Faça um programa que receba a medida do ângulo formado por uma escada apoiada no chão e a distância em que a escada está da parede, calcule e mostre a medida da escada para que se possa alcançar sua ponta.
from math import cos, degrees 

medida_angulo = int(input("Informe medida do ângulo formado pela escada: "))
distancia_parede = int(input("Informe distância em que a escada está da parede: "))

medida_escada = distancia_parede / degrees(cos(medida_angulo))

print("A  medida da escada para que se possa alcançar sua ponta é %2.f" % medida_escada) 