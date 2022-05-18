num_horas_extras = int(input()) * 60 #transformar horas em minutos
num_horas_falta = int(input()) * 60

h = num_horas_extras - (2 / 3 * num_horas_falta)

if (h >= 2400):
    gratificacao_natal = 500
elif (h > 1800 and h < 2400):
    gratificacao_natal = 400
elif (h >= 1200 and h < 1800):
    gratificacao_natal = 300
elif (h >= 600 and h < 1200):
    gratificacao_natal = 200
else:
    gratificacao_natal = 100

print(gratificacao_natal)