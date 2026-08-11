distancia = float(input('Distancia em km: '))
consumo_medio = float(input('Consumo medio em km/l: '))
preco_combustivel = float(input('Preço do combustivel: '))

def custo_viagem(distancia, consumo_medio, preco_combustivel):
    custo = distancia/consumo_medio * preco_combustivel
    return custo


custo_d_viagem = custo_viagem(distancia, consumo_medio, preco_combustivel)

print (custo_d_viagem)





    