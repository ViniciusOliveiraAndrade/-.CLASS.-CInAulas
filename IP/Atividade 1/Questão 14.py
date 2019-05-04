a = int(input("Digite o primeiro número\n> "))
b = int(input("Digite o segundo número\n> "))

if a <= b:
	mmc = a
	for i in range(a,0,-1):
		if a%i==0 and b%i==0 and i!= 1:
			mmc = i 
else:
	mmc = b
	for i in range(b,0,-1):
		if a%i==0 and b%i==0 and i!= 1:
			mmc = i 

print("O Mínimo Múltiplo Comum (MMC) é: {}".format(mmc))