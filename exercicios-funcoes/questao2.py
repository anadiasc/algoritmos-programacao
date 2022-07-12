def converter_segundos(horas, minutos, segundos):
    s_horas = horas * 3600
    s_minutos = minutos * 60
    total = s_horas + s_minutos + segundos
    print(total)
