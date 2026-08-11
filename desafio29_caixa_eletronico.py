velocidade = float(input('Qual a velocidade do carro em Km? '))


if velocidade > 80:
    print('MULTADO! excedeu a velocidade permitida')
    multa = (velocidade - 80) * 7
    print(f'Voce pagara uma multa de R$ {multa :.2f} pelo km excedidos')
else:
    print('Parabens! Voce nao excedeu a velocidade!') 