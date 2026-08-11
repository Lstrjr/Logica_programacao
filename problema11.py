tempoJogo = input() .split()

hi = int(tempoJogo[0])
hf = int(tempoJogo[1])

if hi < hf:
    hj = hf - hi
else:
    hj = 24 - hi + hf
print(f'O JOGO DUROU {hj} HORA(S)')