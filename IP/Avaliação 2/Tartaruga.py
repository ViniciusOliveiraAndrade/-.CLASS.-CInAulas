def ler_aqrquivo_comandos(diretorio):
	comandos = []
	erro = 0
	try:
		arq = open(diretorio,"r")
		for c in arq.readlines():
			c = c.split(" ")
			qt = len(c)-1
			c[qt] = c[qt].replace("\n","")
			comandos.append(c)
	except IOError as e:
		print ("Diretorio nao encontrado")
		erro=1
	except ValueError:
		print ("Algum dado do arquivo não é inteiro!")
		erro=2
	except:
		print ("Aconteceu algum erro grave.")
		erro=3
	if erro == 0:
		if comandos[len(comandos)-1][0]!="6":
			comandos.append(["6"])
	return comandos, erro

def imprime_matriz(matriz):
	print("-----------------------------------------------------------------------------")
	for linha in matriz:
		print('| ', end="")
		for coluna in  linha:
			if coluna == 0:
				print(". ",end="")
			else:
				print("* ",end="")

		print('|')
	print("-----------------------------------------------------------------------------")

def iniciar_matriz():
	colunas = 25
	matriz = [0]*colunas
	for x in range(colunas):
		matriz[x]=[0]*colunas
	return matriz

def iniciar_tartaruga():
	canetaCima = True
	direita = False
	esquerda = False
	cima = False
	baixo = True
	x = 12
	y = 12
	return canetaCima, direita, esquerda, cima, baixo, x, y

def move_tartaruga(matriz,saltos,direita,esquerda,cima,baixo,X,Y,caneta):
	s = saltos
	x = X
	y = Y
	rascunho = matriz
	if esquerda:
		while x > -1 and saltos > 0:
			if not caneta:
				rascunho[y][x] = 1
			saltos -= 1
			x-=1
	elif direita:
		while x < 25 and saltos > 0:
			if not caneta:
				rascunho[y][x] = 1
			saltos -= 1
			x+=1
	elif cima:
		while y > -1 and saltos > 0:
			if not caneta:
				rascunho[y][x] = 1
			saltos -= 1
			y-=1
	elif baixo:
		while y < 25 and saltos > 0:
			if not caneta:
				rascunho[y][x] = 1
			saltos -= 1
			y+=1
	
	if x < 0:
		x+=1
	
	elif x > 24:
		x-=1
	
	if y < 0:
		y+=1
	
	elif y > 24:
		y-=1
	
	return rascunho,x,y

diretorio = input("Digite o diretorio do arquivo, ou FIM para sair.\n>")
while diretorio.lower()!= "fim":
	canetaCima, direita, esquerda, cima, baixo, y, x = iniciar_tartaruga()
	rascunho = iniciar_matriz()
	comandos, erro = ler_aqrquivo_comandos(diretorio)
	if erro < 1:
		i = 0
		while comandos[i][0]!="6":
			if comandos[i][0]=="1":
				canetaCima=True
			elif comandos[i][0]=="2":
				canetaCima=False
			elif comandos[i][0]=="3":
				if direita:
					direita=False
					baixo=True
				elif baixo:
					baixo=False
					esquerda=True
				elif esquerda:
					esquerda=False
					cima=True
				else:
					cima=False
					direita=True

			elif comandos[i][0]=="4":
				if direita:
					direita=False
					cima=True
				elif cima:
					cima=False
					esquerda=True
				elif esquerda:
					esquerda=False
					baixo=True
				else:
					baixo=False
					direita=True

			elif comandos[i][0]=="5":
				rascunho,x,y = move_tartaruga(rascunho,int(comandos[i][1]),direita,esquerda,cima,baixo,x,y,canetaCima)
			i += 1
	if erro == 0:
		print("Rascunho do Arquivo: {}".format(diretorio))
		imprime_matriz(rascunho)
	diretorio = input("Digite o diretorio do arquivo, ou FIM para sair.\n>")
