def ejercicio_1(lista1, lista2):
    lista = []
    if len(lista1) < len(lista2):
        len(lista) == len(lista1)
    else:
        len(lista) == len(lista2)
    for i in range(len(lista1)):
        contador = 0
        if lista1[i] % lista2[i] > 1:
            contador = lista1[i]
        elif lista1[i] % lista2[i] <= 1:
            contador = lista2[i]
    return lista


list1 = [1, 3, 5, 9, 2, 8, 8, 5, 8]
list2 = [8, 4, 2, 6, 5, 7, 3]

valor = ejercicio_1(list1, list2)
print(valor)