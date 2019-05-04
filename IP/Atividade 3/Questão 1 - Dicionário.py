tabela = {}
cod = int(input("Digite um código do curso, ou digite 0 para parar.\n>"))
while cod > 0:
	nome = input("Digite o nome do curso.\n>")
	centro = int(input("Digite número do centro.\n>"))
	
	tabela[cod] = (nome,centro)

	cod = int(input("\n\nDigite um código do curso, ou digite 0 para parar.\n>"))
	while cod in tabela:
		cod = int(input("Digite um código de curso nao cadastrado, ou digite 0 para parar.\n>"))

qt = 0
centro = int(input("Digite número do centro, ou digite 0 para parar.\n>"))
while centro > 0:
	for i in tabela:
		if tabela[i][1] == centro:
			print("Código do curso: {} \t\tNome do curso: {}".format(i,tabela[i][0])) 
			qt+=1
	if qt < 1:
		print("Nenhum curso encontrado")

	centro = int(input("Digite número do centro, ou digite 0 para parar.\n>"))
