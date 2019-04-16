def calcularA(n):
	somaFor = 1
	a = 3
	b = 2
	for i in range(n):
		somaFor += (a/b)
		a += 2
		b += 1

	somaWhile = 1
	a = 3
	b = 2
	i=0
	while i<n:
		somaWhile += (a/b)
		a += 2
		b += 1
		i+=1
	return somaFor,somaWhile


def calcularB(n):
	somaFor = 0
	a = 2
	b = 500
	for i in range(n):
		if (b==0):
			print("6)b. Impossivel dividir por '0'(Zero). \t Ultimo nivel de interacao: {}. \t Ultimo resultado: {}".format(i,somaFor))
			break
		somaFor += (a/b)-((a+3)/(b-10))
		b-=20
	

	somaWhile = 0
	a = 2
	b = 500
	i=0
	while i<n:
		if (b==0):
			print("6)b. Impossivel dividir por '0'(Zero). \t Ultimo nivel de interacao: {}. \t Ultimo resultado: {}".format(i,somaFor))
			break
		somaWhile += (a/b)-((a+3)/(b-10))
		b-=20
		i+=1
	return somaFor,somaWhile

def calcularC(n):
	somaFor = 0
	a = 37
	b = 38
	for i in range(n):
		somaFor += ((a*b)/(i+1))
		a -= 1
		b -= 1

	somaWhile = 0
	a = 37
	b = 38
	i=0
	while i<n:
		somaWhile += ((a*b)/(i+1))
		a -= 1
		b -= 1
		i+=1
	return somaFor,somaWhile



n = int(input("Digite o valor de 'n'\n> "))

For, While = calcularA(n)
print("6)a.\n\tResultado do 'for' é: {}\n\tResultado do 'while' é: {}".format(For, While))

For, While = calcularB(n)
print("\n6)b.\n\tResultado do 'for' é: {}\n\tResultado do 'while' é: {}".format(For, While))

For, While = calcularC(n)
print("\n6)c.\n\tResultado do 'for' é: {}\n\tResultado do 'while' é: {}".format(For, While))