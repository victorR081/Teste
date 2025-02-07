a = float(input())
b = float(input())
c = 180 - (a+b)
if a < 90 and b < 90 and c < 90:
  print("acutangulo")
elif a > 90 or b > 90 or c > 90:
  print("obtusangulo")
else:
  print("retangulo")
