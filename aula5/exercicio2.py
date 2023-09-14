print("0,0 < 3.0 = reprovado "
      ">=3.0 < 7 = exame "
      ">=7 <=10 = aprovado")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = ((nota1 + nota2 + nota3) / 3)
print(f"sua média é: , {media:4.2f}")
if media < 3:
    print("reprovado")
else:
    if media < 7:
        print("exame")
        nota_exame= 12 - media
    else:
        print("aprovado")