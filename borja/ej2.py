temp = [
	((2, 6), (1, 8), (5, 7), (4, 7), (2, 7), (2, 4), (1, 2)),
	((2, 6), (1, 8), (5, 9), (4, 7), (2, 7), (2, 4), (1, 2)),
	((2, 6), (1, 8), (5, 5), (4, 7), (2, 10), (2, 3), (1, 5))
]

def maxmima_semada(temperaturas):
	lista = []
	contador = 0
	for i in range(len(temperaturas)):
		for j in range(len(temperaturas[i])):
			for k in range(len(temperaturas[i][j])):
				if contador < temperaturas[i][j][k]:
					contador = temperaturas[i][j][k]
		lista.append(contador)
		contador = 0
	return lista

print(maxmima_semada(temp))