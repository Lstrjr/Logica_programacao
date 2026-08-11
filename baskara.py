a, b, c = map(float, input(). split())

delta = b**2-4*a*c

x1 = (-b+delta**0.5)/(2*a)
x2 = (-b-delta**0.5)/(2*a)

print (f'{x1:.3f} {x2:.3f}')




