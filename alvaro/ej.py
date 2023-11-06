imagen = [
	[255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
	[255, 0, 0, 0, 0, 0, 255, 255, 255, 255],
	[255, 255, 255, 255, 150, 150, 150, 255, 255, 255],
	[255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
	[255, 10, 10, 10, 255, 255, 255, 255, 255, 255],
	[255, 255, 44, 44, 44, 44, 44, 44, 44, 44],
	[255, 255, 255, 255, 250, 250, 250, 255, 255, 255]
]

magnitud = 100

# ---

def delete_from_list(lista, valor_a_eliminar):
	# Elimina los elementos de una lista que coincidan con el valor dado
	# Devuelve la lista original modificada
	while valor_a_eliminar in lista:
		lista.remove(valor_a_eliminar)