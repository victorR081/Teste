altura = float(input())
peso = float(input())
imc = peso / (altura*altura)
#< 16                Magreza grave
#16 a < 17       Magreza moderada
#17 a < 18,5    Magreza leve
#18,5 a < 25    Saudavel
#25 a < 30       Sobrepeso
#30 a < 35       Obesidade Grau I
#35 a < 40       Obesidade Grau II (severa)
#≥ 40                Obesidade Grau III (morbida)
if imc < 16:
  print("Magreza grave")
elif imc < 17:  # imc >= 16 and imc < 17
  print("Magreza moderada")
elif imc < 18.5:
  print("Magreza leve")
elif imc < 25:
  print("Saudavel")
elif imc < 30:
  print("Sobrepeso")
elif imc < 35:
  print("Obesidade Grau I")
elif imc < 40:
  print("Obesidade Grau II (severa)")
else:
  print("Obesidade Grau III (morbida)")
