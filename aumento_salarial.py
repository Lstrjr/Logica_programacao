salario = float(input())

if salario <= 400.00:
    porcentagem = 15
elif salario <= 800.00:
    porcentagem = 12
elif salario <= 1200.00:
    porcentagem = 10
elif salario <= 2000.00:
    porcentagem = 7
else:
    porcentagem = 4

reajuste = salario*porcentagem/100
novo_salario = salario+reajuste

print(f'Novo salario: {novo_salario:.2f}')
print(f'Reajuste ganho: {reajuste:.2f}')
print(f'Em percentual: {porcentagem} %')