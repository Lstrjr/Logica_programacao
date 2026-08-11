lanche = input() .split()

codigo = int(lanche[0])
quantidade = int(lanche[1])

if codigo == 1:
    total =  quantidade * 4.00

elif codigo == 2:
    total =  quantidade * 4.50

elif codigo == 3:
    total = quantidade * 5.00

elif codigo == 4:
    total = quantidade * 2.00

elif codigo == 5:
    total =  quantidade * 1.50

print(f'Total: R$ {total:.2f}')