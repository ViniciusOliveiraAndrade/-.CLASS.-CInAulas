def carregarPro():
	tabelaPro={}
	pro = open("pro.arq")
	for p in pro:
		p = p.split(";")
		tabelaPro[int(p[0])] = p[1].replace("\n","")
	pro.close()
	return tabelaPro

def pergarC(arq):
	try:
		cod = int(input("\nDigite o codigo da profissao, ou um numero menor que 1 para sair\n>"))
	except Exception as e:
		print("\n-----------------------------------\nDigite um numero inteiro!!!\n-----------------------------------\n")
		return pergarC(arq)
	arq.write("{}\n".format(cod))
	return cod

profissoes = carregarPro()
codigosDigitatos = open("codigos.odl", "a")
cod = pergarC(codigosDigitatos) 

while cod > 0:
	if cod in profissoes:
		print("\nNome: {}\n".format(profissoes[cod]))
	else:
		print("\nProfissao Inexistente!\n")

	cod = pergarC(codigosDigitatos)