numero = int(input("Digite um número. \n>"))
i = 1
while numero % i != 0 and i < numero:
	i+=1

if i != numero:
	print("O número '{}' nao é primo".format(numero))
else:
	print("O número '{}' é primo".format(numero))
