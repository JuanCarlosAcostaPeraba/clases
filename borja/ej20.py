def list_reader(list_len):
	list = []
	if not isinstance(list_len, int):
		raise TypeError("The input must be an integer")
	if list_len <= 0:
		raise ValueError("The input must be a positive integer")
	while list_len > 0:
		try:
			value = int(input("Enter a value: "))
			list.append(value)
			list_len -= 1
		except ValueError:
			print("The value must be an integer")
	return list

print(list_reader(5))