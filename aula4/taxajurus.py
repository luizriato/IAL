deposito = float(input("Digite o valor do deposito: "))
jurus = float(input("Digite a taxa de jurus em porcentagem(apenas os numeros): "))
meses = float(input("Digite a quantidade de meses aplicado: "))
valoratual = deposito + (deposito * (jurus / 100) * meses)
print("Seu valor atual é de: ", valoratual)
print("Seu rendimento foi de:", valoratual - deposito)

