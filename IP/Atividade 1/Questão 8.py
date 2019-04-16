inicio = int(input("Digite o valor de inicio(Não incluso)\n> "))
termino = int(input("Digite o valor de término(Não incluso)\n> "))


for i in range(inicio+1,termino):
	print("Grau em Celsius do Fahrenheit {}° do 'for' é: {}".format(i,(i-32)*5/9))

print("\n")
i = inicio+1
while i <termino:
	print("Grau em Celsius do Fahrenheit {}° do 'while' é: {}".format(i,(i-32)*5/9))
	i+=1

