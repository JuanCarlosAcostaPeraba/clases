def ejercicio_5(a):
	lista = []
	contador = 0
	for i in range(len(a)):
		for j in range(len(a[i])):
			x = (a[i][j] - 1, a[i][j]+ 1)
			a[i][j] = x
	lista = a
	return lista

lista = [
	[1,3,5,9],
	[8,4,2,5,6]
]

print(ejercicio_5(lista))