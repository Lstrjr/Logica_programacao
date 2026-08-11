soma = 0

denominador = 50

for expoente in range(1, 51):  # 1 até 50
    termo = (2 ** expoente) / denominador
    soma += termo
    denominador -= 1

print("Resultado da soma:", soma)