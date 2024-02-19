
def load(name_file):
	try:
		lista = []
		with open(name_file, 'r') as file:
			for line in file:
				lista2 = []
				words = line.split()
				for word in words:
					lista2.append(int(word))
				lista.append(lista2)
		return lista
	except FileNotFoundError:
		return "El archivo no existe"
