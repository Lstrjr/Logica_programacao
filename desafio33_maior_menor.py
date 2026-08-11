a = int(input('primeiro valor: '))
b = int(input('segundo valor: '))
c = int(input('terceiro valor: '))

menor = a
if b < a and b < c:
    menor = b
elif c < a and c < b:
    menor = c

maior = a

if b > a and b > c:
    maior = b

elif c > a and c > b:
    maior = c

print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')