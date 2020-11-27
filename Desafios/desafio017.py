from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h = hypot(co, ca)
print(f'A hipotenuza de um triangulo retangulo de cateto oposto {co} e')
print(f'cateto adjacente {ca} vale {h:.2f}')
