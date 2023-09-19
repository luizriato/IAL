largura = float(input("Digite a largura do local: "))
comprimento = float(input("Digite o comprimento do local: "))
tinta = (int(input("Digite a quantidade de litros da lata de tinta: ")) * 3)
pe_direito = 2.80
porta = 1.68
parede1 = (largura - 0.80) * (pe_direito - 2.80)
parede2 = largura * pe_direito
parede3 = comprimento * pe_direito
parede4 = comprimento * pe_direito
print ("a quantidade de latas de tinta necessária é: ", (parede1 + parede2 + parede3 + parede4) / tinta)



