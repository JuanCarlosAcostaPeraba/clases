def iniciales():
		with open("t.txt", "r") as f, open("t2.txt", "w") as f2:
				for line in f:
						for word in line.split():
								f2.write(word[0])
						f2.write("\n")

iniciales()
