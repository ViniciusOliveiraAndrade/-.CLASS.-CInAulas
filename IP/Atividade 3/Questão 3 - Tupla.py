def verificar(cod,lista):
	for i in lista:
		if i[0]==cod:
			return True
	else:
		return False

tabela = []
cpf = int(input("Digite um CPF da pessoa, ou digite um numero negativo para parar.\n>"))
while cpf > -1 and len(tabela) < 201:
	nome = input("Digite o nome da pessoa.\n>")
	idade = int(input("Digite a idade.\n>"))
	
	tabela.append((cpf,nome,idade))

	cpf = int(input("\n\nDigite um CPF da pessoa, ou digite um numero negativo para parar.\n>"))
	while verificar(cpf, tabela):
		cpf = int(input("Digite um CPF da pessoa nao cadastrada, ou digite um numero negativo para parar.\n>"))

n = int(input("Digite o número de intervalos de idades.\n>"))
mini = int(input("Digite a idade mínima.\n>"))
maxi = int(input("Digite a idade máxima.\n>"))
while maxi < mini:
	maxi = int(input("Digite a idade máxima válida e maior que a minima que é: {}.\n>").format(mini))


for i in range(n):
	qt = 0
	for pessoa in tabela:

		if pessoa[2] >= mini and pessoa[2] <= maxi :
			print("CPF da pessoa: {} \t\tNome da pessoa: {}\t\tIdade da pessoa: {}".format(pessoa[0],pessoa[1],pessoa[2])) 
			qt+=1

	print("Quantidade de pessoas: {}".format(qt))
	mini = int(input("Digite a idade mínima.\n>"))
	maxi = int(input("Digite a idade máxima.\n>"))
	while maxi < mini:
		maxi = int(input("Digite a idade máxima válida e maior que a minima que é: {}.\n>").format(mini))