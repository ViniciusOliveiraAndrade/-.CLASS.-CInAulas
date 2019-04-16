n = int(input("Digite um número\n>"))
soma = 0
for i in range(1,n):
	if n % i == 0:
		soma+=i

if soma == n:
	print("O número ' {} ' é perfeito".format(soma))
else:
	print("O número ' {} ' nao é perfeito".format(n))
