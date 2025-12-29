# beecrowd - 1010 Cálculo Simples

_, qtd1, peca1 = map(float, input().split())
_, qtd2, peca2 = map(float, input().split())

valor_total = (qtd1 * peca1) + (qtd2 * peca2)

print(f'VALOR A PAGAR: R$ {valor_total:.2f}')