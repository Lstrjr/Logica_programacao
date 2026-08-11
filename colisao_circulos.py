from math import sqrt

def test_colisao(x1, y1, raio1, x2, y2, raio2):
    distancia = sqrt((x2-x1)**2 + (y2 - y1)**2)
    soma_raio = raio1 + raio2
    if distancia <= soma_raio:
        return True
    else:
        return False
    
cx1 = int(input('Coordenada x do círculo 1 '))
cy1 = int(input('Coordenada y do círculo 1 '))
raio1 = int(input('Raio do círculo 1 '))
cx2 = int(input('Coordenada x do círculo 2 '))
cy2  = int(input('Coordenada y do círculo 2 '))
raio2  = int(input ('Raio do círculo 2 '))

colisao = test_colisao(cx1, cy1, raio1, cx2, cy2, raio2)

print(colisao)
