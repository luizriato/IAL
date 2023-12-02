def animals(h, f):
    rabbit  = (f - 2 * h ) / 2
    duck = h - rabbit
    return (rabbit,duck)

head = int(input("Digite o total de cabeças: "))
foot = int(input("Digite o total de pés: "))
patos , coelhos = animals(head, foot)
print(f"O número de patos é {patos}, o número de coelhos é: {coelhos}")