#Python 3
def fat(n):
	if n < 2:
		return 1
	else:
		return n * fat(n-1)

def serie(n): #Estou utilizando python3 entao nao necessario deixar explacito que o denomidaor é float. Ele sabera..
	a = 10
	b = 1
	s = 0
	if n < 1:
		return s
	else:
		for i in range(1,n+1):
			if i%2==1:
				s+=a/fat(b)
			else:
				s-=a/fat(b)
			a+=5
			b+=1
		return s


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

def imprimi(n,res):
	print("O valor da serie com %d termos e %.4f"%(n,res))
	return

qtd = pergarInteiro("\nDigite a quantidade de vezes que deseja calcular o valor da serie.\n>", "Digite um numero inteiro apenas!!")
series = [None]*qtd
for i in range(qtd):
	n = pergarInteiro("\nDigite o numero de termos da serie que deseja calcular.\n>", "Digite um numero inteiro apenas!!")
	series[i]=n	
series.sort(reverse=True)
for n in series:
	imprimi(n, serie(n))