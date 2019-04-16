soma = 0
qt = 3
tipo = int(input("Digite 1 para números reáis e qualquer outro para números inteiro\n> "))
for i in range(qt):
	if tipo == 1: 
		numero = input("Digite o {}° número\n> ".format(i+1))
		numero = float(numero.replace(",","."))

	else: 
		numero = int(input("Digite o {}° número\n> ".format(i+1)))
	soma +=numero

media = soma/qt
print("A média é {}".format(media))