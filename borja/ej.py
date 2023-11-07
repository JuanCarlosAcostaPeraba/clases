lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7, 8, 9]

def max(lista1, lista2):
		lista = []

		if len(lista1) > len(lista2):
			mayor = lista1
			menor = lista2
		else:
			mayor = lista2
			menor = lista1

		for i in range(len(mayor)):
			if i < len(menor):
				if mayor[i] > menor[i]:
					lista.append(mayor[i])
				elif mayor[i] < menor[i]:
					lista.append(menor[i])
			else:
				if mayor[i] > -1:
					lista.append(mayor[i])
				elif mayor[i] < -1:
					lista.append(-1)
		
		return lista

max(lista1, lista2)
