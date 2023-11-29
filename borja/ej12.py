def min(lista):
	'''Devuelve el menor de los elementos de la lista l con recursividad'''
	if len(lista) == 1:
		return lista[0]
	else:
		if lista[0] < min(lista[1:]):
			return lista[0]
		else:
			return min(lista[1:])

print(min([1, -4, 5, 2, 6, 10]))
