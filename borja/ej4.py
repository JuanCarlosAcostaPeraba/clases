def transpose(lista1):
	lista = []
	for j in range(len(lista1[0])): # columnas
		lista.append([])
		for i in range(len(lista1)): # filas
			lista[j].append(lista1[i][j])
	return lista
		

print(transpose([[1,2,3],[4,5,6]]))
