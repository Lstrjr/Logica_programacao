ano = int(input('digite um ano'))
if (ano % 4 ==0 and ano % 100 != 0) or (ano %400 ==0):
    print(f'O ano e {ano} e bissexto')
else:
    print(f'O ano de {ano} nao  e bissexto')

