from random import randint

randomNumbers = (

randint(0, 10),
randint(0, 10),
randint(0, 10),
randint(0, 10),
randint(0, 10)

)

print('Numeros gerados: \n')

for c in randomNumbers:
	print(c)

print(f'''\nMaior número: {sorted(randomNumbers)[-1]}
Menor número: {sorted(randomNumbers)[0]}''')
