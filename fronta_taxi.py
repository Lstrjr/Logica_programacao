
f = input() .split()

A = float((f[0]))
G = float((f[1]))
RA = float((f[2]))
RG = float((f[3]))


AbastecerA = A / RA
AbastecerG = G / RG

if AbastecerA < AbastecerG:
    print ('A')

else:
    print('G')