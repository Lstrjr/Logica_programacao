
def imc(peso, altura):
    r = peso/(altura*altura)
    return r

def class_imc(valor_imc):
    if valor_imc < 16:
        resultado = 'Magreza extrema'
    elif valor_imc < 17:
        resultado = 'Magreza moderada'
    elif valor_imc < 18.5:
        resultado = 'Magreza leve'
    elif valor_imc < 25:
        resultado = 'Saudavel'
    elif valor_imc < 30:
        resultado = 'Sobrepeso'
    elif valor_imc < 35:
        resultado = 'Obesidade grau I'
    elif valor_imc < 40:
        resultado = 'Obesidade grau II'
    else:
        resultado = 'Obesidade grau 3 (morbida)'
    return resultado

peso = int(input('Digite seu peso em kg: ')) 
altura = float(input('Digite sua altura: '))

valor = imc(peso, altura)
classificaçao = class_imc(valor)

print(f'{valor:.2f}')
print(classificaçao)




        


     