def word_frec(string1):
	dic = {}
	chars = "abcdefghijklmnopqrstuvwxyz"
	palabra = ""
	for line in string1:
		for word in line.split():
			if word.lower() in dic:
				dic[word.lower()] += 1
				continue
			else:
				dic[word.lower()] = 1
			for char in word.lower():
				if char in chars:
					palabra += char
				else:
					break
			if palabra == "":
				continue
			if palabra in dic:
				dic[palabra] += 1
			else:
				dic[palabra] = 1
	for key in sorted(dic.keys()):
		print(f"{key},{dic[key]}\n")

string = ["HOla como estas, hola bien y tú?", "mi número es 123, llamame/o"]
word_frec(string)

# --
'''
def words_frec(file1: str, file2: str):
    with open(file1, "r") as file_r, open(file2, "w") as file_w:
        abecedario = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        dic: dict = {}
        line = file_r.readline()
        palabra = ""
        while line:
            for letter in line:
                if letter in abecedario:
                    palabra += letter
                else:
                    if palabra.lower() in dic:
                        dic[palabra.lower()] = dic[palabra.lower()] + 1
                        palabra = ""
                        continue
                    else:
                        if palabra == "":
                            continue
                        else:
                            dic[palabra.lower()] = 1
                            palabra = ""
                            continue
            if palabra.lower() in dic:
                dic[palabra.lower()] = dic[palabra.lower()] + 1
                palabra = ""
            else:
                if palabra != "":
                    dic[palabra.lower()] = 1
                    palabra = ""
            line = file_r.readline()
        sort_list = sorted(dic.items())
        for keys, values in sort_list:
            print(f"{keys},{values}", end="\n", file=file_w)
'''