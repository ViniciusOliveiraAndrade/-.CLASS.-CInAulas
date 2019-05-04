tabela = {}
cod = int(input("Digite um código da pessoa, ou digite um numero negativo para parar.\n>"))
while cod > -1:
	nome = input("Digite o nome da pessoa.\n>")
	salario = input("Digite o salário da pessoa.\n>")
	salario = float(salario.replace(",", "."))

	
	tabela[cod] = (nome,salario)

	cod = int(input("\n\nDigite um código da pessoa, ou digite um numero negativo para parar.\n>"))
	while cod in tabela:
		cod = int(input("Digite um código da pessoa nao cadastrada, ou digite um numero negativo para parar.\n>"))

qt = 0
media = 0
salarioMaximo = input("Digite o salário máximo.\n>")
salarioMaximo = float(salarioMaximo.replace(",", "."))
while salarioMaximo < 0:
	salarioMaximo = input("Digite o salário máximo.\n>")
	salarioMaximo = float(salarioMaximo.replace(",", "."))

for i in tabela:
	if tabela[i][1] <= salarioMaximo:
		print("Código da pessoa: {} \t\tNome da pessoa: {}\t\tSalário da pessoa: {}".format(i,tabela[i][0],tabela[i][1])) 
		qt+=1
		media += tabela[i][1]

print("Quantidade de pessoas: {}".format(qt))
print("Média dos salário: {}".format(media/qt))
