preco = float(input('Qual o preço do seu produto? '))

novo = preco - (preco*5 / 100)

print('o produto que custava R$ {}, na promoçao com desconto de 5% vai custar R${}'.format(preco, novo))