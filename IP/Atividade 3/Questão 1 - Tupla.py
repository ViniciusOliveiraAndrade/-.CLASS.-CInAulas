def verificar(cod,lista):
	for i in lista:
		if i[0]==cod:
			return True
	else:
		return False

tabela = []
cod = int(input("Digite um código do curso, ou digite 0 para parar.\n>"))
while cod > 0:
	nome = input("Digite o nome do curso.\n>")
	centro = int(input("Digite número do centro.\n>"))
	tabela.append((cod,nome,centro))

	cod = int(input("\n\nDigite um código do curso, ou digite 0 para parar.\n>"))
	while verificar(cod, tabela):
		cod = int(input("Digite um código de curso nao cadastrado, ou digite 0 para parar.\n>"))

qt = 0
centro = int(input("\nDigite número do centro, ou digite 0 para parar.\n>"))
while centro > 0:
	for i in tabela:
		if i[2] == centro:
			print("Código do curso: {} \t\tNome do curso: {}".format(i[0],i[1])) 
			qt+=1
	if qt < 1:
		print("Nenhum curso encontrado")

	centro = int(input("Digite número do centro, ou digite 0 para parar.\n>"))
