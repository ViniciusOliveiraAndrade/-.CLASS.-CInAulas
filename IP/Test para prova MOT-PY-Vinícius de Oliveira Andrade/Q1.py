def pergarInteiro():
	try:
		inteiro = int(input("\nDigite um numero, ou um numero menor que 1 para sair\n>"))
	except Exception as e:
		print("\n-----------------------------------\nDigite um numero inteiro!!!\n-----------------------------------\n")
		return pergarInteiro()
	return inteiro

n = pergarInteiro()
while n > 0:
	aux = 2
	a = 100
	b = 20
	s = a/b
	print(" ({}/{})".format(a,b), end=" ")
	
	a+=30
	b+=10
	while aux <= n:
		if aux % 2 == 0:
			s -= (a/b)
			print("- ({}/{})".format(a,b), end=" ")
			a+=10
			b+=10
		else: 
			s += (a/b)
			print("+ ({}/{})".format(a,b), end=" ")
			a+=30
			b+=10
		aux += 1
	print("A soma do {}° termo é: {}".format(n,s))
	n = pergarInteiro()
