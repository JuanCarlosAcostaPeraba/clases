def merge(l1, l2):
	if len(l1) == 0:
		return l2
	elif len(l2) == 0:
		return l1
	elif l1[0] < l2[0]:
		return [l1[0]] + merge(l1[1:], l2)
	else:
		return [l2[0]] + merge(l1, l2[1:])
	
print(merge([1, 4, 5], [2, 6, 10]))