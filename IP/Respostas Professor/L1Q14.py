def MMC(a,b):
	if a == 1 or b == 1:
		return 1
	res = 2
	while a % res != 0 or b % res != 0:
		res += 1
	return res 