lista = []
i = 0
while i > -1 and len(lista)<1001:
	i = int(input("Digite o valor.\n>"))
	if i > 9:
		lista.append(i)

print (lista[::-1])
