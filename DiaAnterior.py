dia = int(input())
mes = int(input())
ano = int(input())
#                    1   2   3   4   5   6   7   8   9   10  11  12
ultimoDiaDoMes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if isBissexto(ano):
  ultimoDiaDoMes[2] = 29

dia = dia - 1
if dia == 0:
  mes = mes - 1
  if mes == 0:
    mes = 12
    ano = ano - 1
  dia = ultimoDiaDoMes[mes]

print("%d %d %d" % (dia, mes, ano))
