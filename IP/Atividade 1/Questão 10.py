qt = int(input("Digite a quantidade de números a ser convertido.\n> "))

romanos = ""
for i in range(qt):
	numero = int(input("Digite o número a ser convertido para algarismos romanos.\n> "))
	aux = numero
	while numero != 0:
		if numero >= 1000:
			numero -= 1000
			romanos +="M"
		
		elif numero >= 900:
			numero -= 900
			romanos += "CM"

		elif numero >= 500:
			numero -= 500
			romanos += "D"

		elif numero >= 400:
			numero -= 400
			romanos += "CD"

		elif numero >= 100:
			numero -= 100
			romanos += "C"

		elif numero >= 90:
			numero -= 90
			romanos += "XC"

		elif numero >= 50:
			numero -= 50
			romanos += "L"

		elif numero >= 40:
			numero -= 40
			romanos += "XL"
		
		elif numero >= 10:
			numero -= 10
			romanos += "X"

		elif numero >= 9:
			numero -= 9
			romanos += "IX"

		elif numero >= 5:
			numero -= 5
			romanos += "V"

		elif numero >= 4:
			numero -= 4
			romanos += "IV"

		elif numero >= 1:
			numero -= 1
			romanos += "I"

	print("O número ' {} ' em algarismos romanos é: {}".format(aux,romanos))
	romanos=""