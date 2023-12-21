def no_white_lines(file1, file2):
	with open(file1, "r") as file_r, open(file2, "w") as file_w:
		for line in file_r:
			if line.strip() == "":
				continue
			else:
				file_w.write(f"{line}")
				continue
