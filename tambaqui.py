P1, P2, X1, C1 = map(float, input(). split())
Q1, Q2, X2, C2 = map(float, input(). split())
R1, R2, X3, C3 = map(float, input(). split())


valor1 = P1 + P2
pix1 = valor1 - (valor1*X1/100)
cart1 = valor1 + (valor1*C1/100)
if pix1 < cart1:
    BANCA1 = pix1
else:
    BANCA1 = cart1

valor2 = Q1 + Q2
pix2 = valor2 - (valor2*X2/100)
cart2 = valor2 + (valor2*C2/100)
if pix2 < cart2:
    BANCA2 = pix2
else:
    BANCA2 = cart2

valor3 = R1 + R2
pix3 = valor3 - (valor3*X3/100)
cart3 = valor3 + (valor3*C3/100)
if pix3 < cart3:
    BANCA3 = pix3
else:
    BANCA3 = cart3

if BANCA1<=BANCA2 and BANCA1<=BANCA3:
     print(f"R$ {BANCA1:.2f} Banca 1")
elif BANCA2<=BANCA1 and BANCA2<=BANCA3:
     print(f"R$ {BANCA2:.2f} Banca 2")
elif BANCA3<=BANCA1 and BANCA3<=BANCA2:
     print(f"R$ {BANCA3:.2f} Banca 3")


