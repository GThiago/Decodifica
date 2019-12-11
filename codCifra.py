import sys

key = sys.argv[1]
frase = sys.argv[2]

tam = len(key)
i = 0

for letra in frase:
	if i >= tam:
		i = 0
		
	if letra == " ":
		newletter = 32
		i-=1
	else:
		newkey = ord(key[i]) - 65
		newletter = ord(letra) + newkey
		if newletter > 90:
			newletter = newletter - 26

	print(chr(newletter), end="")
	i+=1
print()
