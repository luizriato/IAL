idade = int(input("digite a sua idade: "))
if 5 < idade <= 7:
    print("infantil")
elif idade <= 10:
    print("juvenil")
elif idade <=15:
    print("adolescente")
elif idade <= 30:
    print("adulto")
else:
    print("sênior")