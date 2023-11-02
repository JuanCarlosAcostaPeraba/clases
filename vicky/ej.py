def maxima_semana(parámetro):
	x = []
	tempmax = 0
	for i in range(len(parámetro)):
		for j in range(len(parámetro[i])):
			for k in range(len(parámetro[i][j])):
				if tempmax < parámetro[i][j][k]:
					tempmax = parámetro[i][j][k]
		x.append(tempmax) # meter en lista
		tempmax = 0
	return x

lista = [
	((6, 2),(2,0),(4,3)),
	((3,2), (2, 1), (3,2)),
	((3,2), (10, 1), (3,2))
	]

print(maxima_semana(lista))