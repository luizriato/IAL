def primo(numero):
    for c in range(2, 1+(numero//2)):
        if numero == c:
            pass
        if numero % c == 0:
            return False
    return True


def count(numero):
    primo1= 0;
    for c in range(numero+1):
        if primo(c):
            primo1 += 1
    return primo1

def soma(numero):
    total = 0
    for c in range(numero+1):
        if primo(c):
            total += c
    return total


value = int(input("Digite um número inteiro e positivo: "))
print(f"De 0 a {value} existem {count(value)} números primos")
print(f"A soma dos números primos é: {soma(value)}")