

massa = float(input('eeee: '))

etapa = 0
tempo_final = 0
while massa >= 0.5:
    massa /= 2 #massa / 2
    etapa += 1 # etapa + 1
    tempo_final = etapa * 40 #tempo += 40
    print(massa)

horas = tempo_final // 3600
minutos = (tempo_final % 3600) // 60
segundos = tempo_final % 60


print(horas)
print(minutos)
print(segundos)

