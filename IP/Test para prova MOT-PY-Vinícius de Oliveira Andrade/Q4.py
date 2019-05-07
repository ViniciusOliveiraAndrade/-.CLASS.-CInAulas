def lerArquivoFuncionario():
	funcionarios = {}
	arq = open("funcionarios.csv")
	for i in arq.readlines():
		i=i.split(";")
		matricula = int(i[0])
		sexo = int(i[1])
		salario = float(i[2])
		nome = i[3]
		funcionarios[matricula] = (sexo,salario,nome)
	return funcionarios

def criarArquivo(funcionarios,valor):
	qt = 0
	media = 0
	arq = open("graduados.csv","w")
	for f in funcionarios:
		if funcionarios[f][1] > valor:
			arq.write("{};{}\n".format(f,funcionarios[f][1]))
			qt += 1
			media += funcionarios[f][1]
	return qt, (media/qt)

def pergarInteiro(msg):
	try:
		inteiro = int(input("\n{}\n>".format(msg)))
	except Exception as e:
		print("\n-----------------------------------\nDigite um numero inteiro!!!\n-----------------------------------\n")
		return pergarInteiro()
	return inteiro

f = lerArquivoFuncionario()
print(f)
Num1 = pergarInteiro("Digite o Valor maximo da media")
qt, media = criarArquivo(f, Num1)
print("Quantidade de no arquivo entrada: {}\n Quantidade de no arquivo saida: {}\nMédiados salarios: {}\n".format(len(f),qt,media))