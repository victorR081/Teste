#Soma números positivos a cada entrada, quanto digita um negativo ele interrompe e na saída temos o resultado da soma
e = int(input())
soma = 0
while e > 0:
  soma = soma + e
  e = int(input())
print(soma)
