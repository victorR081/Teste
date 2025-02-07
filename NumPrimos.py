# Digite um número na entrada e ele diz se é um número composto ou primo
n = int(input())
cont = 1
for i in range(2, n+1):  # i = 2 .. n
    if n % i == 0:
      cont = cont + 1  # contador de divisores
if cont == 2:
  print("PRIMO")
else:
  print("COMPOSTO")
