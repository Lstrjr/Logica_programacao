temperatura = float(input('Digite uma temperatura em Celsius: '))
c = temperatura

def converC():
    F = (c * 9/5) + 32.
    return F

f = converC()

print(f'a temperatura em Celsius convertida em Fahrenheit: {f}')

temperatura1 = float(input('Digite a temperatura em Fahrenheit: '))

def converF():
    C = (temperatura1 - 32) * 5/9
    return C

A = converF()

print(f'A temperatura em Fahrenheit convertida para  Celsius: {A} ')

