from random import randint
computador = randint(0, 10)

jogador = int(input("Qual o numero que estou pensando? "))

if computador == jogador:
    print ("Parabens! Voce acertou")
else: 
    print(f"Voce errou! O numero que pensei foi o {computador} e o numero que vc digitou foi {jogador}")