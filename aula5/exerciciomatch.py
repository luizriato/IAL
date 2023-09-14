dia = int(input("digite o número do dia da semana:"))
match dia:
    case 1:
        nome = "domingo"
    case 2:
        nome = "segunda"
    case 3:
        nome = "terça"
    case 4:
        nome = "quarta"
    case 5:
        nome = "quinta"
    case 6:
        nome = "sexta"
    case 7:
        nome = "sábado"
if dia < 7:
    print(nome)
else:
    print("digite um número de 1 a 7")

