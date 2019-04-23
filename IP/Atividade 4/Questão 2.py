def contrario(n):
	return "".join(list(str(n))[::-1])

def contar():
	i = 100
	while i < 5001:
		if contrario(i) == str(i):
			print("O número {} é Palídromo.".format(i))
		i+=1
contar()