matr1 = [
	[1,1],
	[1,1]
]
matr2 = [
	[1,1],
	[1,1]
]

def sum(matr1, matr2):
	x = []
	lista = []
	contador = 0
	for i in range(len(matr1)):
		x = []
		for j in range(len(matr1[i])):
			x.append(matr1[i][j] + matr2[i][j])
		lista.append(x)
	return lista

print(sum(matr1, matr2))