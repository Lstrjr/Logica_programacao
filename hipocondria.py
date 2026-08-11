h1, m1, s1  = map(int, input(). split())
h2, m2, s2  = map(int, input(). split())

hora1 = (h1*3600)+(m1*60)+s1
hora2 = (h2*3600)+(m2*60)+s2

hora_final = hora2 - hora1

print(f'{hora_final} segundo(s)')