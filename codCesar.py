import sys

dec = list(sys.argv[1])

for x in range(27):
	print(x)
	for letra in dec:
		if letra == " ":
			print(end=" ")
		else:
			print(chr(ord(letra)-x), end="")
		
	print()
	
