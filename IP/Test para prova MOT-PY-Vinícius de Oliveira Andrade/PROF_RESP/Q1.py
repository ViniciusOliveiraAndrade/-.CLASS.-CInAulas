def serie(n):
	ni = 100
	np = -130
	d = 20
	res = 0
	for i in range(1,n+1):
		if i % 2 == 1:
			res = res + ni/d
			ni = ni + 40
			d = d + 10
		else:
			res = res + np/d
			np = np - 30
			d = d + 10
	return res

def pergarInteiro():
	try:
		inteiro = int(input("\nDigite um numero, ou um numero menor que 1 para sair\n>"))
	except Exception as e:
		print("\n-----------------------------------\nDigite um numero inteiro!!!\n-----------------------------------\n")
		return pergarInteiro()
	return inteiro

n = pergarInteiro()
while n > 0:
	r = serie(n)
	print("A soma do {}° termo é: {}".format(n,r))
	n = pergarInteiro()
