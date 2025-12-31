# beecrowd - 1018 Cédulas

n = int(input())

valor = n

notas = [100, 50, 20, 10, 5, 2, 1]

print(n)

for nota in notas:
    quantidade = valor // nota
    print(f'{quantidade} nota(s) de R$ {float(nota):.2f}'.replace('.', (',')))
    valor = valor % nota