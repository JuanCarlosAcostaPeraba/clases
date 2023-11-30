def aprobados(data, code):
	lista = []
	for clave, valor in data[2][code].items():
		if valor >= 5:
			lista.append(data[1][clave])
	lista.sort()
	return lista

def nota_media(data, name):
	media = 0
	counter = 0
	for dni, nombre in data[1].items():
		if nombre == name:
			for asignatura, nota_data in data[2].items():
				media += nota_data[dni]
				counter += 1
	return media / counter

def datos_por_asignatura(data):
	lista = []
	for code_asignatura, data_asignatura in data[0].items():
		for code_alumno, data_alumno in data[1].items():
			if data[2][code_asignatura][code_alumno] >= 5:
				lista.append([data_alumno, data_asignatura[0], data_asignatura[2]])
			else:
				lista.append([data_alumno, data_asignatura[0], 0])
	return lista

def semestre(data, semestre):
	d = {}
	for code_asignatura, data_asignatura in data[0].items():
		if data_asignatura[1] == semestre:
			d[data_asignatura[0]] = 0
			for dni, nota in data[2][code_asignatura].items():
				if nota >= 5:
					d[data_asignatura[0]] += 1
	return d

					

data = (
	{
		"123": ("ABC", 2, 6),
		"456": ("DEF", 1, 12)
	},
	{
		"40": "Pepe",
		"30": "Alvaro"
	},
	{
		"123": {"40": 5, "30": 4},
		"456": {"40": 7, "30": 5}
	}
)

print(aprobados(data, "456"))
print(nota_media(data, "Pepe")) # 5 + 7 / 2 = 6
print(datos_por_asignatura(data))
print(semestre(data, 1))