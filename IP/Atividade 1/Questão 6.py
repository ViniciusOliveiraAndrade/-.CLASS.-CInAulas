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
		somaFor += (a/b)-((a+3)/(b-10))
		b-=20

	somaWhile = 0
	a = 2
	b = 500
	i=0
	while i<n:
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



n = int(input("\nDigite o valor de 'n' para a questao 6)a.\n> "))

For, While = calcularA(n)
print("\tResultado do 'for' é: {}\n\tResultado do 'while' é: {}".format(For, While))

n = int(input("\nDigite o valor de 'n' para a questao 6)b.\n> "))
while n >25:
	n = int(input("\nDigite o valor de 'n' menor que 26 para a questao 6)b.\n> "))
For, While = calcularB(n)
print("\tResultado do 'for' é: {}\n\tResultado do 'while' é: {}".format(For, While))

n = int(input("\nDigite o valor de 'n' para a questao 6)c.\n> "))
For, While = calcularC(n)
print("\tResultado do 'for' é: {}\n\tResultado do 'while' é: {}".format(For, While))