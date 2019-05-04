aux = float(input("Digite um valor.\n>"))
soma = aux
qt = 1
while aux>=0:
	aux = input("Digite um valor\n> ")
	aux = float(aux.replace(",","."))
	soma += aux
	qt += 1

print("A média aritmética é: {}".format(soma/qt))