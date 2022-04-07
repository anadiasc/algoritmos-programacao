# Faça um programa que receba uma hora (uma variável para hora e outra para minutos), calcule e mostre: a) a hora digitada convertida em minutos; b) o total dos minutos, ou seja, os minutos digitados mais a conversão anterior; c) o total dos minutos convertidos em segundos.

hora = int(input())
minutos = int(input())

hora_para_minutos = hora * 60
total_minutos = minutos + hora_para_minutos
minutos_para_segundos = total_minutos * 60

print("a hora digitada convertida em minutos: %d \ntotal dos minutos: %d \nminutos convertidos em segundos: %d" % (hora_para_minutos, total_minutos, minutos_para_segundos))