# RAM LIMITADA 512 números de 32 bits
# evitar cosas raras
# no existe entrada de usuario

def compile(file, out):
	f = open(file, "r")
	lines = f.readlines()
	outlines = []
	for i in range(len(lines)):
		outlines.append(translate(lines[i]))
	f.close()
	ff = open(out, "w")
	for line in outlines:
		ff.write(line)
def translate(texto):
	return texto

fi = "nada.txt"
ou = "salida.txt"

compile(fi, ou)
