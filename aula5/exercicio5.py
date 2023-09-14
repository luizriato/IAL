ano_nascimento = int(input("digite o ano de nascimento: "))
ano_atual = int(input("digite o ano atual: "))
idade = ano_atual - ano_nascimento
print("você tem", idade,"anos")
if idade >= 16:
    print("Você já tem idade para votar")
else:
    print("Você ainda não tem idade para votar")
if idade >= 18:
    print("você já pode tirar a habilitação")
else:
    print("você ainda não pode tirar habilitação")
