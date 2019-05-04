def carregarCentros():
	tabelaCentros={}
	centros = open("centros.arq")
	for centro in centros:
		centro = centro.split(";")
		tabelaCentros[centro[0]] = centro[1]
	centros.close()
	return tabelaCentros

def gravarDisciplinas(c,diciplinas):
	qtD = 0
	saida = open("discipCompleto.arq","w")
	for linha in diciplinas.readlines():
		linha = linha.split(";")
		cod = linha[0]
		nome = linha[1]
		cre = int(linha[2])
		nomeC = c[str(int(linha[3]))]
		codC = int(linha[3])
		qtD += 1
		saida.write("{},{},{},{},{}\n".format(cod,nome,cre,codC,nomeC.replace("\n","")))

	saida.close()
	return qtD

d = open("discip.arq")
c = carregarCentros()
qt = gravarDisciplinas(c,d)
d.close()

print("Número de diciplinas: {}\nNúmero de centros: {}".format(qt,len(c)))