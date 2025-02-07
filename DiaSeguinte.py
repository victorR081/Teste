# 3 entradas, dia, mes e ano. Digite os 3 e ele volta na sáida o dia seguinte.
dia = int(input())
mes = int(input())
ano = int(input())

#                    1   2   3   4   5   6   7   8   9   10  11  12
ultimoDiaDoMes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if isBissexto(ano):
  ultimoDiaDoMes[2] = 29

dia = dia + 1
if dia > ultimoDiaDoMes[mes]:
  dia = 1
  mes = mes + 1
  if mes > 12:
    mes = 1
    ano = ano + 1
print("%d %d %d" % (dia, mes, ano))
