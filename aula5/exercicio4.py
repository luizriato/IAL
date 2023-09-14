altura = float(input("digite a altura em metros, exemplo 1.80: "))
sexo = (input("digite o sexo m ou f: "))
if sexo == "m":
    print("seu peso ideal é", 72.7 * altura - 58)
else:
    print("seu peso ideal é: ", 62.1 * altura - 44.7)

