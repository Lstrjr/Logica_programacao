impureza = float(input('soluçao em: '))
inicial = impureza
tempo = 0

while impureza >= inicial*0.02 and impureza <1800:
    impureza *= 0.85
    tempo +=25

print(impureza)
print(tempo)

hora = tempo //3600
minuto = (tempo % 3600)//60
segundo = tempo % 60

print(hora)
print(minuto)
print(segundo)
