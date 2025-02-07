#Dígite um valor em reais que ele volta quantas cédulas de cada valor são necessárias como um Caixa Eletrônico.
n = int(input())
print("R$%d.00" % n)
n100 = n // 100
n = n % 100
n50 = n // 50
n = n % 50
n20 = n // 20
n = n % 20
n10 = n // 10
n = n % 10
n5 = n // 5
n = n % 5
n2 = n // 2
n1 = n % 2
print("%d nota(s) de R$100.00" % n100)
print("%d nota(s) de R$50.00" % n50)
print("%d nota(s) de R$20.00" % n20)
print("%d nota(s) de R$10.00" % n10)
print("%d nota(s) de R$5.00" % n5)
print("%d nota(s) de R$2.00" % n2)
print("%d nota(s) de R$1.00" % n1)
