def validar_senha(senha):
    
    if len(senha) < 8:
        return False

    tem_maiuscula = False
    tem_numero = False

    # Verificando cada caractere da senha
    for caractere in senha:
        if caractere.isupper():
            tem_maiuscula = True
        if caractere.isdigit():
            tem_numero = True
    if tem_maiuscula and tem_numero:
        return True
    else:
        return False


# Programa principal
senha = input("Digite uma senha para validar: ")

if validar_senha(senha):
    print("Senha válida!")
else:
    print("Senha inválida! A senha deve ter pelo menos 8 caracteres, 1 letra maiúscula e 1 número.")
