a = float(input())
b = float(input())
c = 180 - (a+b)
# acutangulo retangulo obtusangulo
if a == 90 or b == 90 or c == 90:
  print("retangulo")
elif a > 90 or b > 90 or c > 90:
  print("obtusangulo")
else:
  print("acutangulo")
