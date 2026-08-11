r1 = float(input('Primeira segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('os segmentos foram triangulo')
else:
    print('Os segmentos NAO formam triangulos')