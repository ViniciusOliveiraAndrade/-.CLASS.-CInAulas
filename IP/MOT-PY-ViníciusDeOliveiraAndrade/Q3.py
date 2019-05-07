#Python 3
def pergarInteiro(msg1,msg2):
	n = 0
	try:
		n = int(input(msg1))
		return n
	except Exception as e:
		print("\n----------------------------------------------------------------")
		print(msg2)
		print("----------------------------------------------------------------")
		return pergarInteiro(msg1, msg2)

def pergarReal(msg1,msg2):
	n = 0
	try:
		n = float(input(msg1).replace(",", "."))
		return n
	except Exception as e:
		print("\n----------------------------------------------------------------")
		print(msg2)
		print("----------------------------------------------------------------")
		return pergarInteiro(msg1, msg2)

def imprimeMatriz(matriz):
	print("---------------------------------------------------------")
	for linha in matriz:
		print("| ",end="")
		for coluna in linha:
			print("%f "%(coluna), end="")
		print("|")
	print("---------------------------------------------------------")

def diagonal(m,n):
	qt = 0
	mult = 1
	for i in range(n):
		for j in range(n-i,n):
			if m[i][j] != 0:
				mult *= m[i][j]
				qt+=1
	if qt == 0:
		return 0
	else:
		return mult

def lerMatriz(n):
	matriz = [None]*n
	qt = 0
	for i in range(n):
		matriz[i]=[None]*n
		for j in range(n):
			matriz[i][j]=pergarReal("\nDigite um numero Real.\n>", "Digite um numero Real apenas!!")
			if matriz[i][j]%2 != 0:
				if qt == 0:
					maior = matriz[i][j]
					qt +=1
				elif matriz[i][j] > maior:
					maior = matriz[i][j]


	imprimeMatriz(matriz)
	print("A multiplicacai dos elementos nao nulos da abaixo da diagonal secundaria e: {}".format(diagonal(matriz,n)))
	if qt != 0:
		print("Maior impar e: {}".format(maior))
	else:
		print("Nao ha numeros imares na matriz")


n = pergarInteiro("\nDigite um numero.\n>", "Digite um numero inteiro apenas!!")
while n<5 or n>20:
	n = pergarInteiro("\nDigite um numero >=5 ou <=20.\n>", "Digite um numero inteiro apenas!!")
lerMatriz(n)
