n = int(input("Digite o valor de 'N'\n> "))

termoInicial = -1

for i in range(n):
	print("{}° Termo da sequência pelo 'for': {}".format(i+1,termoInicial))
	if((i+1)%2==0):
		termoInicial += 5
	else:
		termoInicial += 1

print("\n")

termoInicial = -1
i =0
while i < n:
	print("{}° Termo da sequência pelo 'while': {}".format(i+1,termoInicial))
	if((i+1)%2==0):
		termoInicial += 5
	else:
		termoInicial += 1
	i+=1