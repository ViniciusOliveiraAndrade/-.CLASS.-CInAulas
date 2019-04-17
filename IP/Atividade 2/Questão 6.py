n = int(input("Digite o tamanho da lista.\n>"))

lista = []
pares = []
impares = []

for i in range(n):
	lista.append(int(input("Digite o {}° Valor do 1° vetor.\n>".format(i+1))))

for j in lista:
	if j % 2 == 0:
		pares.append(j)
	else:
		impares.append(j)
print("Lista de Valores Informado: {}".format(lista))
print("Lista de Valores Impares: {}".format(impares))
print("Lista de Valores Pares: {}".format(pares))