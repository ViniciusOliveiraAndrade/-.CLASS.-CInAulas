a = int(input("Digite o 1°\n> "))
b = int(input("Digite o 2°\n> "))

if b == 0:
	print ("Impossível a divisão por '0' (Zero)")

else:
	resto = a % b
	if resto == 0:
		print("Primério número é :{}".format(a))
	else:
		quadrado = resto ** 2
		print("O quadrado do resto é :{}".format(quadrado))

