def evaluate(t):
	if type(t) == tuple:
		if t[1] == '+':
			return evaluate(t[0]) + evaluate(t[2])
		elif t[1] == '-':
			return evaluate(t[0]) - evaluate(t[2])
		elif t[1] == '*':
			return evaluate(t[0]) * evaluate(t[2])
		elif t[1] == '/':
			return evaluate(t[0]) / evaluate(t[2])
	else:
		return t


print(evaluate(((56, '+', (5, '*', 2)), '/', (12, '-', 2))))
