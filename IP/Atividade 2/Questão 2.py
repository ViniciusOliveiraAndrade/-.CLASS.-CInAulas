nome = input("Digite seu nome.\n>")

for i in range(len(nome)):
	print("{} Letra: {}".format(i+1,nome[:i+1]))