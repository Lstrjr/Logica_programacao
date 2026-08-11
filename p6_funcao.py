
def analisar_texto(texto):
    nun_caracteres = len(texto) #retorna o numero de itens em um objeto como caracteres
    nun_palavras = len(texto.split()) #len +.split divide o texto em palavras (separadas por espaços)
    return nun_caracteres, nun_palavras

texto = str(input('Digite uma texto: '))

r = analisar_texto(texto)

print(r)


