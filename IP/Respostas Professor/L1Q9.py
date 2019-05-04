def serie9(n):
	res = -1
	for i in range(2,n+1):
		if i % 2 == 0:
			res += 1
		else:
			res += 5
	return res

n = int(input(">"))
while n < 1:
	n = int(input(">"))
valor = serie9(n)
print("Termo da serie: {}".format(valor))