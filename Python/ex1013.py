# beecrowd - 1013 O Maior

a, b, c = map(int, input().split())

maiorAB = (a + b + abs(a - b)) // 2
maior_numero = (maiorAB + c + abs(maiorAB - c)) // 2

print(f'{maior_numero} eh o maior')