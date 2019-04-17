m = int(input("Digite o valor de M.\n>"))
while m < 5 and m > -1:
	m = int(input("Digite um valor valido de M.\n>"))
	
n = int(input("Digite o valor de N.\n>"))
while n < 5 and n > -1:
	n = int(input("Digite um valor valido de N.\n>"))
	
matriz = []

for i in range(m):
	matriz.append([])
	for j in range(n):
		