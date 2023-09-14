numero1 = int(input("digite o primeiro numero: "))
numero2 = int(input("digite o segundo numero: "))
print("1. Média entre os números digitados "
      "2 Diferença do maior pelo menor "
      "3 Produto entre os números digitados "
      "4 Divisão do primeiro pelo segundo ")
opcao = input("digite a opção desejada: ")
if opcao == "1":
    media = ((numero1 + numero2) / 2)
    print(media)
if opcao == "2":
    if numero1 > numero2:
        print(numero1 - numero2)
    else:
        print(numero2 - numero1)
if opcao == "3":
    print(numero1 * numero2)
else:
    print(numero2 / numero1)
if opcao == "4":
    print(numero1 / numero2)
