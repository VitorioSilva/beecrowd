# beecrowd - 1008 Salário

numero_funcionario = int(input())
horas_trabalhadas = int(input())
valor_por_hora = float(input())

salario_funcionario = horas_trabalhadas * valor_por_hora

print(f'NUMBER = {numero_funcionario}')
print(f'SALARY = U$ {salario_funcionario:.2f}')