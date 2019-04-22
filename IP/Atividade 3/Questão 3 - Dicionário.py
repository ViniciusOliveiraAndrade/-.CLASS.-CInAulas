tabela = {}
cpf = int(input("Digite um CPF da pessoa, ou digite um numero negativo para parar.\n>"))
while cpf > -1 and len(tabela) < 201:
	nome = input("Digite o nome da pessoa.\n>")
	idade = int(input("Digite a idade.\n>"))
	
	tabela[cpf] = (nome,idade)

	cpf = int(input("\n\nDigite um CPF da pessoa, ou digite um numero negativo para parar.\n>"))
	while cpf in tabela:
		cpf = int(input("Digite um CPF da pessoa nao cadastrada, ou digite um numero negativo para parar.\n>"))

n = int(input("Digite o número de intervalos de idades.\n>"))
mini = int(input("Digite a idade mínima.\n>"))
maxi = int(input("Digite a idade máxima.\n>"))
while maxi < mini:
	maxi = int(input("Digite a idade máxima válida e maior que a minima que é: {}.\n>").format(mini))


for i in range(n):
	qt = 0
	for cpf in tabela:

		if tabela[cpf][1] >= mini and tabela[cpf][1] <= maxi :
			print("CPF da pessoa: {} \t\tNome da pessoa: {}\t\tIdade da pessoa: {}".format(cpf,tabela[cpf][0],tabela[cpf][1])) 
			qt+=1

	print("Quantidade de pessoas: {}".format(qt))
	mini = int(input("Digite a idade mínima.\n>"))
	maxi = int(input("Digite a idade máxima.\n>"))
	while maxi < mini:
		maxi = int(input("Digite a idade máxima válida e maior que a minima que é: {}.\n>").format(mini))