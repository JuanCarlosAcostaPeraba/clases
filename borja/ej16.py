def export_dic(dic, file):
		# ordenar diccionario por clave en orden alfabetico
		dic_sorted = dict(sorted(dic.items()))
		with open(file, 'w') as f:
			for key, value in dic_sorted.items():
				f.write(f'{key},')
				for i in range(len(value)):
					f.write(f'{value[i]}')
					if i < len(value) - 1:
						f.write(',')
				f.write('\n')
