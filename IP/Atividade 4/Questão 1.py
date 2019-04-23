def quebrar(n):
	n = str(n)
	l = []
	for x in n:
		l.append(int(x))
	return l

def imprime_qt(numero,n=9):
	lista = quebrar(numero)
	qt = 0
	for i in lista:
		if i == n:
			qt+=1
	print("A quantidade de {} no número: {} é: {}".format(n,numero,qt))

def lerNumero():
	numero = int(input("Digite um número.\n>"))
	if numero < 1:
		return
	elif numero > 99999:
		print("Valor inválido! Limite de 99999")
		lerNumero()
	else:
		imprime_qt(numero)
		lerNumero()

def lerNumeros():
	numero = int(input("Digite um número.\n>"))
	if numero < 1:
		return
	elif numero > 99999:
		print("Valor inválido! Limite de 99999")
		lerNumeros()
	else:
		p = int(input("Digite um número para ser procurado.\n>"))
		imprime_qt(numero,p)
		lerNumeros()
		
lerNumero()

print("\n\n")

lerNumeros()