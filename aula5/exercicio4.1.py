x = int(input("digite o valor de x: "))
y = int(input("digite o valor de y: "))
z = int(input("digite o valor de z: "))
if (x < y +z) and (y < x + z) and (z < x + y):
    if (x == y) and (y == z):
        print("triângulo equilátero")
    elif (x == y) or (y == z) or (x == z):
        print("triângulo isósceles")
    else:
        print("triângulo escaleno")
else:
    print("não é possivel executar a conta")