viagem = float(input('Qual a distancia da viagem: '))
if viagem <= 200:
    preco = viagem * 0.50
else:
    preco = viagem *0.45
print(f'O custo da viagem sera de {preco}')
