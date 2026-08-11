def calcular_preco_final(valor_original):
    if (valor_original >= 200 and valor_original <= 499.99):
        novo_valor = valor_original - (valor_original * 0.10)
    elif (valor_original >= 500):
        novo_valor = valor_original - (valor_original * 0.15 )
    else:
        novo_valor = valor_original
    return novo_valor

valor = float(input('Digite o valor da compra: '))
preco_final = calcular_preco_final(valor)

print(preco_final)