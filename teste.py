def contar_numeros():
    """
    Lê números até que o usuário digite 0 e conta quantos números foram inseridos.
    """
    contador = 0
    numero = -1  # Inicializamos com um valor diferente de 0 para entrar no loop

    print("Digite números inteiros. Digite 0 para encerrar.")
    
    # Loop principal: continua enquanto o número digitado não for 0
    while numero != 0:
        try:
            # Pede a entrada do usuário
            numero = int(input(f"Digite o {contador + 1}º número (ou 0 para parar): "))
            
            # Se o número não for 0, incrementa o contador
            if numero != 0:
                contador += 1
                
        except ValueError:
            # Trata o caso em que o usuário insere algo que não é um número
            print("Entrada inválida. Por favor, digite apenas números inteiros.")

    # Exibe o resultado final
    print(f"\n--- FIM ---")
    print(f"Você digitou um total de **{contador}** números (excluindo o 0 de parada).")

# Chama a função para rodar o programa
v = contar_numeros()
print(vocv)