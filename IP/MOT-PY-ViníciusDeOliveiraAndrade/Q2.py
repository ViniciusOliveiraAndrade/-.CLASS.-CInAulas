#Python 3
def pergarInteiro(msg1,msg2):
	n = 0
	try:
		n = int(input(msg1))
		return n
	except Exception as e:
		print("\n----------------------------------------------------------------")
		print(msg2)
		print("----------------------------------------------------------------")
		return pergarInteiro(msg1, msg2)

def pegarInteiroMenor1():
	n = pergarInteiro("\nDigite um numero negativo.\n>", "Digite um numero inteiro apenas!!")
	while n>0:
		n = pergarInteiro("\nDigite apenas um numero negativo ou zero para parar.\n>", "Digite um numero inteiro apenas!!")
	return n

numeros = []
n = pegarInteiroMenor1()
qt = 0
maior = n
while n < 0:
	numeros.append(n)
	if n > maior and n%11==0:
		maior=n
	qt += 1
	n = pegarInteiroMenor1()
print("Quantidade total de numeros negativos digitados: %d"%(qt))

#Python3 ignora qualquer 0 a esqueda automaticamente
qt3di = 0
s = 0
print("Numeros com 3 digitos significativos: ",end="")
for numero in numeros[::-1]:
	if numero < -99:
		print("%d, "%(numero), end="")
		qt3di+=1
		s+=numero
if qt3di == 0:
	print("\nMedia aritimetica dos numeros de 3 digitos significativos: 0")
else:
	media = s/qt3di
	print("\nMedia aritimetica dos numeros de 3 digitos significativos: %f"%(media))

if maior%11==0:
	print("Maior numero lido multiplo de 11 é: %d"% maior)
else: 
	print("Nao ha maior numero multiplo de 11.")