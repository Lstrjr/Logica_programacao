p1, p2, x1, c1 = map(float, input().split())
q1, q2, x2, c2 = map(float, input().split())
r1, r2, x3, c3 = map(float, input().split())

total1 = p1 + p2
pix1 = total1 * (1 - x1 / 100)
cartao1 = total1 * (1 + c1 / 100)
if pix1 < cartao1:
    banca1_melhor = pix1
else:
    banca1_melhor = cartao1

# --- Cálculos Banca 2 ---
total2 = q1 + q2
pix2 = total2 * (1 - x2 / 100)
cartao2 = total2 * (1 + c2 / 100)
if pix2 < cartao2:
    banca2_melhor = pix2
else:
    banca2_melhor = cartao2

# --- Cálculos Banca 3 ---
total3 = r1 + r2
pix3 = total3 * (1 - x3 / 100)
cartao3 = total3 * (1 + c3 / 100)
if pix3 < cartao3:
    banca3_melhor = pix3
else:
    banca3_melhor = cartao3

# --- Comparação Final entre as Bancas ---
if banca1_melhor <= banca2_melhor and banca1_melhor <= banca3_melhor:
    valor_final = banca1_melhor
    nome_banca = "Banca 1"
elif banca2_melhor <= banca1_melhor and banca2_melhor <= banca3_melhor:
    valor_final = banca2_melhor
    nome_banca = "Banca 2"
else:
    valor_final = banca3_melhor
    nome_banca = "Banca 3"

# Saída formatada
print(f"R$ {valor_final:.2f} {nome_banca}")