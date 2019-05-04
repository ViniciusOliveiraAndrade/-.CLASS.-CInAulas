entrada = open("discip.old")
saida = open("discip.new", "w")

qtEntrada = 0
qtSaida = 0
qtCredito = 0

for linha in entrada.readlines():
	l = linha.split(";")
	qtEntrada += 1
	if l[0] != "IF125" and l[0] != "IF380":
		qtSaida += 1
		if l[0].find("MA",0,2)!= -1:
			saida.write("{};{};{};{}\n".format(l[0], l[1], 5, int(l[2])*15))
		else:
			saida.write("{};{};{};{}\n".format(l[0], l[1], int(l[2]), int(l[2])*15))
			qtCredito+=1

print("Número de diciplinas no arquivo 'discip.old': {}\nNúmero de diciplinas no arquivo 'discip.old': {}\nNúmero de diciplinas com creditos alterdos: {}".format(qtEntrada,qtSaida,qtCredito))
