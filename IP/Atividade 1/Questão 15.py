numero = int(input("Digite um número:"))
dot = 0
for i in range(2,numero):
	if numero%i==0:
		dot+=1

if dot != 0:
	print("O número ' {} ' nao é primo".format(numero))
else:
	print("O número ' {} ' é primo".format(numero))
