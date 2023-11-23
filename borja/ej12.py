def min(l):
	'''Devuelve el menor de los elementos de la lista l con recursividad'''
	if len(l) == 1:
		return l[0]
	else:
		if l[0] < min(l[1:]):
			return l[0]
		else:
			return min(l[1:])
		
print(min([1, -4, 5, 2, 6, 10]))