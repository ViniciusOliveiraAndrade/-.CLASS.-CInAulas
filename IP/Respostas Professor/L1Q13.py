def MDC(a,b):
	if a < b:
		res = a
	else:
		res = b
	while a % res != 0 or b % res != 0:
		res -= 1
	return res 