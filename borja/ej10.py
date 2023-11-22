def filter_names(names, letter):
	if len(names) == 0:
		return []
	elif names[0][0] == letter:
		return [names[0]] + filter_names(names[1:], letter)
	else:
		return filter_names(names[1:], letter)
	
print(filter_names(['Borja', 'Juan', 'Pedro', 'Pablo', 'Belen', 'Berta'], 'B'))
