def emparejados(a, b, c):
	# {1,2,3,4,5}, {1,3,4,5}, {1,2,3,4} -> {2,5}
	# {1,2}, {1,3}, {1,2} -> {2}
	
	# interseccion de 2 diccionarios
	interseccion = (a & b) - c | (a & c) - b | (b & c) - a
	return interseccion

print(emparejados({1,2,3,4,5}, {1,3,4,5}, {1,2,3,4})) # {2,5}