nome = input("Digite seu nome.\n>")

for i,letra in enumerate(nome):
	print("{}° Letra: {}".format(i+1,letra))