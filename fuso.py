S, T, F = map(int, input() .split())

horaTotal = S + T + F

if horaTotal >= 24:
    horaTotal = horaTotal - 24
elif horaTotal < 0:
    horaTotal = 24 + horaTotal
print(horaTotal)




