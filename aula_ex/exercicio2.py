valor_compra = float(input("Digite o valor da compra: "))
if valor_compra <= 1000:
    print("o desconto será de 10%")
else:
    if valor_compra > 1000 and valor_compra<= 5000:
        print("o desconto será de 20%")
    else:
        print("o desconto será de 30%")