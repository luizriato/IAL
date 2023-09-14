salario = float(input("digite seu salário atual: "))
aumento = float(input("digite seu aumento em porcentagem(apenas os numeros): "))
aumento = aumento / 100
salarionovo = salario + salario * aumento
print("seu novo salario é: ", salarionovo)
print("seu aumento foi de: ", salarionovo - salario)