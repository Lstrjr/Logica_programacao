nome = str(input())
salario_fixo = float(input())
vendas_total = float(input())

salario_final = salario_fixo + vendas_total*0.15

print(f'TOTAL = R$ {salario_final:.2f}')