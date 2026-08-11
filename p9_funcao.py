

def formatar_nome_completo(nome, sobrenome):
    formatar_nome = nome.title()
    formatar_sobrenome = sobrenome.title()
    return f'{formatar_nome} {formatar_sobrenome}'


nome = str(input('Digite o seu nome: '))
sobrenome = str(input('Digite seu sobrenome: '))

nome_completo = formatar_nome_completo(nome, sobrenome)
print(nome_completo)
