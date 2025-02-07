#Verifica se um número é espelho do outro, com 2 entradas
n1 = int(input())
n2 = int(input())

d11 = n1//1000
n1 = n1 % 1000
d12 = n1//100
n1 = n1%100
d13 = n1//10
d14 = n1%10

d21 = n2//1000
n2 = n2 % 1000
d22 = n2//100
n2 = n2%100
d23 = n2//10
d24 = n2%10

if d11==d24 and d12==d23 and d13==d22 and d14==d21:
  print("espelho")
else:
  print("nao espelho")
