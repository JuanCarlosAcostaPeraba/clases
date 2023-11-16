def valores_en_rango(lista, num1, num2):
	dic = set()
	for i in lista:
		if i >= num1 and i <= num2:
			dic.add(i)
	return dic

print(valores_en_rango([1,2,3,4,5,6,7,8,9,10], 3, 7))