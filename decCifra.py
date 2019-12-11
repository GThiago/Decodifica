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
		newkey = ord(letra) - ord(key[i]) 
		if newkey < 0:

			newkey +=26
#		print(" new ",newkey)
		newletter = newkey + 65
#		print(" e ",letra)

	print(chr(newletter), end="")
	i+=1
print()
