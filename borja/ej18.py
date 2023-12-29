def load_list(string):
	lista = []
	with open(string, "r") as f:
		for line in f:
			lista.append(line.split())