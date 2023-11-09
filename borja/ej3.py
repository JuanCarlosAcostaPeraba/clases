def count_values(lista1, lista2):
	for i in range(len(lista2)):
		count = 0
		for j in range(len(lista1)):
			if lista2[i] == lista1[j]:
				count += 1
		lista2[i] = (lista2[i], count)
	return lista2

print(count_values([1, 2, 3, 4, 3, 3, 7, 2, 9], [1, 2, 3]))