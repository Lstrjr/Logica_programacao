contador = 0

while True:
    numero = int(input("Digite um número (0 para parar): "))
    if numero == 0:
        break
    
contador += 1

print("Você digitou", contador, "números.")