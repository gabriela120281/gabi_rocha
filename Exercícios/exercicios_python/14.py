
# 14 Leia uma quantidade de minutos (int) e converta para horas e minutos (ex.: 130 -> 2h10)
minutos = int(135)
horas = minutos // 60
minutos_restantes = minutos % 60
print(f"{minutos} minutos equivalem a {horas} horas e {minutos_restantes} minutos.")
