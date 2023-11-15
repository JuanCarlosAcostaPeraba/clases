def aux(numero):
	letra = int(numero) % 23
	letras = "TRWAGMYFPDXBNJZSQVHLCKE"
	return numero + letras[letra]

# print(aux("78536469"))

# how to import a function from another file
# from ej6 import aux

def changeDNI(dic):
	for key in dic:
		dic[key] = (aux(key), dic[key])
	return dic

print(changeDNI({"78536469": "JC"}))