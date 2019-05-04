m = int(input("Digite o valor de M.\n>"))

while m < 1 or m > 4:
	m = int(input("Digite um valor valido de M.\n>"))
	
n = int(input("Digite o valor de N.\n>"))
while n < 1 and n > 8:
	n = int(input("Digite um valor valido de N.\n>"))
	
matriz = []

for i in range(m):
	matriz.append([])
	for j in range(n):
		matriz[i].append(int(input("Digite o valode da posicao {}X{}.\n>".format(i,j))))

print(matriz)