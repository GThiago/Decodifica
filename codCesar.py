import sys

dec = list(sys.argv[1])

for letra in dec:
	if letra == " ":
		print(end=" ")
	else:
		print(chr(ord(letra)+3), end="")
	
print()
