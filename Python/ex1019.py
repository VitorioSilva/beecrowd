# beecrowd - 1019 Conversão de Tempo

segundos = int(input())

horas = segundos // 3600
segundos = segundos % 3600

minutos = segundos // 60
segundos = segundos % 60

print(f'{horas}:{minutos}:{segundos}')