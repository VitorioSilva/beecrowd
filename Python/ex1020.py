# beecrowd - 1020 Idade em Dias

idade = int(input())

ano = idade // 365
mes = idade % 365

dia = mes % 30
mes = mes // 30

print(f'{ano} ano(s)')
print(f'{mes} mes(es)')
print(f'{dia} dia(s)')