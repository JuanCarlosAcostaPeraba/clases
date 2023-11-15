def join_lists(list1, list2):
		dict1 = {}
		if len(list1) >= len(list2):
			for i in range(len(list2)):
				dict1[list1[i]] = list2[i]
		else:
			for i in range(len(list1)):
				dict1[list1[i]] = list2[i]
		return dict1