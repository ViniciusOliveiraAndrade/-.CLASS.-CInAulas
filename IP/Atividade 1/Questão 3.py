menor = int(input("Digite o 1° número\n> "))
qt = 2

for i in range(qt):
	aux =  int(input("Digite o {}° número\n> ".format(i+2)))
	if aux < menor:
		menor = aux

print("O menor número é :{}".format(menor))