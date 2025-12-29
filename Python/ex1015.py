# beecrowd - 1015 Distância Entre Dois Pontos

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

p1 = (x1, y1)
p2 = (x2, y2)

distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print(f'{distancia:.4f}')