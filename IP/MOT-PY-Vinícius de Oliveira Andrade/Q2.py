def mediaPonderada(a,b,c):
	return ((a*2)+(b*3)+(c*4))/9

def imprime(aluno):
	nome = aluno[0]
	media = mediaPonderada(aluno[1], aluno[2], aluno[3])
	if media > 7:
		print("Aluno '%s' teve média de '%.1f' e possúi a situacao 'A'"%(nome,media))
	elif media > 5:
		print("Aluno '%s' teve média de '%.1f' e possúi a situacao 'B'"%(nome,media))
	else:
		print("Aluno '%s' teve média de '%.1f' e possúi a situacao 'C'"%(nome,media))

def pergarInteiro():
	try:
		inteiro = int(input("\nDigite um numero, ou um numero menor que 1 para sair\n>"))
	except Exception as e:
		print("\n-----------------------------------\nDigite um numero inteiro!!!\n-----------------------------------\n")
		return pergarInteiro()
	return inteiro

def pergarFloat(msg,msg2):
	try:
		floa = input("\n{}\n>".format(msg))
		floa = float(floa.replace(",","."))
		#tem que tratar a nota
	except Exception as e:
		print("\n-----------------------------------\n{}\n-----------------------------------\n".format(msg2))
		return pergarFloat(msg,msg2)
	return floa

n = pergarInteiro()
alunos = [0]*n
for i in range(n):
	alunos[i] = ["",0,0,0]

for i in range(n):
	alunos[i][0] = input("Digite o nome do aluno: ")
	for j in range(3):
		alunos[i][j+1] = pergarFloat("Digite a {}° nota do aluno".format(j+1), "Digite uma nota valida!!! \n Exmplo: 10,0 ou 10.0")
	imprime(alunos[i])