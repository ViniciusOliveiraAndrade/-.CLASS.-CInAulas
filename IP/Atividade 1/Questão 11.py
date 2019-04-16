aux = int(input("Digite um valor.\n> "))
menor = aux
while aux != 0:
	aux = int(input("Digite um valor.\n> "))
	if aux != 0 and aux < menor :
		menor = aux

print("\nMenor valor digitado foi: {}".format(menor))