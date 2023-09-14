from math import sqrt
x1 = float(input("Entre o valor de x1: "))
x2 = float(input("Entre com de x2: "))
y1 = float(input("Entre com o valor de y1: "))
y2 = float(input("Entre com o valor da y2: "))
dx = x2 - x1
dy = y2 - y1
dist = sqrt((dx * dx)+(dy * dy))
print ("a distância entre os pontos é: ", dist)