L, D = input() .split()
K, P = input() .split()
custoKM = int(L) * int(K)
nunPedagio = (int(L) // int(D))
custoPedagio = nunPedagio * int(P)
custoTotal = custoKM + custoPedagio

print(f'{custoTotal}')