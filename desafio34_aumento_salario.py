salario = float(input('Digite seu salario; '))

if salario <=1250:
    aumento = salario + (salario * 15 / 100)
else:
    aumento = salario + (salario * 10 / 100)

print(f'seu novo salario sera de {aumento}')