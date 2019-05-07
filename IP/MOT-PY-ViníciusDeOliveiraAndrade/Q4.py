#Python 3
try:
	disc = open("disciplinas.txt")
	qt = 0
	creditos = 0
	carga = 0
	print("Disciplinas com codigo IF**8:\n")
	for linha in disc.readlines():
		qt+=1
		if linha[:2] == "IF" and linha[4:5] == "8":
			print("Codigo: %s\t Nome: %s"%(linha[:5],linha[13:43]))
			try:
				creditos+=int(linha[6:8])
			except Exception as e:
				print("\nOs creditos da disciplina %s nao sao numeros."%(linha[13:43]))
		try:
			carga+=int(linha[9:12])
		except Exception as e:
			print("\nOs carga da disciplina %s nao sao numeros."%(linha[13:43]))
	print("\nA soma dos creditos das disciplinas de codigo: IF**8 sao: %d"%(creditos))
	if qt>0:
		media = carga/qt
		print("\nA carga horaria media de todas as disciplinas é: %f"%(media))
	else:
		print("\nA carga horaria media de todas as disciplinas é: 0")
	print("\nA quantidade de disciplinas no arquivo é: %d"%(qt))
except IOError as e:
	print("\nArquivo não encontrado")
except Exception:
	print("\nPanico, fuja ou vai morrer!!")

