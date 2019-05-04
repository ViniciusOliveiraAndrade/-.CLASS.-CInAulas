def multiploPrimeiro(A,B,C):
	if A % B ==0 and A % C != 0:
		return True
	else:
		return False

def procedimento(Num1, Num2, Mult1, Mult2):
	qt = 0
	for i in range(Num1,Num2+1):
		if multiploPrimeiro(i, Mult1, Mult2):
			qt+=1
			print("{} é multiplo de {} mas nao de {}".format(i,Mult1,Mult2))
	print("Quantidade de valores: {}".format(qt))

def pergarInteiro(msg):
	try:
		inteiro = int(input("\n{}\n>".format(msg)))
	except Exception as e:
		print("\n-----------------------------------\nDigite um numero inteiro!!!\n-----------------------------------\n")
		return pergarInteiro()
	return inteiro

Num1 = pergarInteiro("Digite o Valor inicial da serie")
Num2 = pergarInteiro("Digite o Valor final da serie")
Mult1 = pergarInteiro("Digite o Valor de Mult1")
Mult2 = pergarInteiro("Digite o Valor de Mult2")
while Mult1 == Mult2:
	Mult2 = pergarInteiro("Digite o Valor de Mult2")
	
procedimento(Num1, Num2, Mult1, Mult2)
procedimento(Num1, Num2, Mult2, Mult1)