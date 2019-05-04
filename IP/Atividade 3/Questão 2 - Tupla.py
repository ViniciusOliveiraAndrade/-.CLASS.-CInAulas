def verificar(cod,lista):
	for i in lista:
		if i[0]==cod:
			return True
	else:
		return False

tabela = []
cod = int(input("Digite um código da pessoa, ou digite um numero negativo para parar.\n>"))
while cod > -1:
	nome = input("Digite o nome da pessoa.\n>")
	salario = input("Digite o salário da pessoa.\n>")
	salario = float(salario.replace(",", "."))

	
	tabela.append((cod,nome,salario))

	cod = int(input("\n\nDigite um código da pessoa, ou digite um numero negativo para parar.\n>"))
	while verificar(cod, tabela):
		cod = int(input("Digite um código da pessoa nao cadastrada, ou digite um numero negativo para parar.\n>"))

qt = 0
media = 0
salarioMaximo = input("Digite o salário máximo.\n>")
salarioMaximo = float(salarioMaximo.replace(",", "."))
while salarioMaximo < 0:
	salarioMaximo = input("Digite o salário máximo.\n>")
	salarioMaximo = float(salarioMaximo.replace(",", "."))

for i in tabela:
	if i[2] <= salarioMaximo:
		print("Código da pessoa: {} \t\tNome da pessoa: {}\t\tSalário da pessoa: {}".format(i[0],i[1],i[2])) 
		qt+=1
		media += i[2]

print("Quantidade de pessoas: {}".format(qt))
print("Média dos salário: {}".format(media/qt))
