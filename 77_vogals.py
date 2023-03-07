words = (

"lapis",
"caneta",
"borracha",
"python",
"CASA"

)

for word in words:

	print(f'\nA palavra {word} tem as vogais ', end='')

	for char in word:

		if char.lower() in 'aeiou':

			print(f'{char.lower()} ', end='')

print('\n\nFIM DO PROGRAMA..')
