def soma(num):
    total = 0
    for c in num:
        total += int(c)
    return total

def multiply(num):
    total = 1
    for c in num:
        total *= int(c)
    return total

number = input("Digite um número inteiro positivo: ")
print(f"A soma dos números é: {soma(number)} e a multiplicação é: {multiply(number)}")
