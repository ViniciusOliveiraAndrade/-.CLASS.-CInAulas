inicio = int(input("Digite o valor de inicio(Não incluso)\n> "))
termino = int(input("Digite o valor de término(Não incluso)\n> "))

soma = 0
for i in range(inicio+1,termino):
	if i % 2 != 0:
		soma += i 
print("Soma do 'for': {}".format(soma))

soma = 0
i = inicio+1
while i <termino:
	if i % 2 != 0:
		soma += i
	i+=1

print("Soma do 'while': {}".format(soma))