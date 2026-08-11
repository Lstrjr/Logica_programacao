

def gerar_email(nome, sobrenome, dominio):
    e = f'{nome.lower()}.{sobrenome.lower()}.@{dominio.lower()}' #.lower deixa as iniciais em minusculo
    return e


nome = str(input('digite seu nome: '))
sobrenome = str(input('Digite seu sobrenome: '))
dominio = str(input('Digite o dominio do ifam: '))

email = gerar_email(nome, sobrenome, dominio)

print(email)
