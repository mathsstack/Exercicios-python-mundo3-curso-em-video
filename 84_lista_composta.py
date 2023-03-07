array = []
auxiliar = []

mpesadas = []
mleves = []

for c in range(0, 5):

	auxiliar.insert(0, input('\nNome: '))
	auxiliar.insert(1, int(input('Peso: ')))

	if c == 0 or auxiliar[1] >= mpesadas[-1][1]:

		mpesadas.append(auxiliar[:])

	if c == 0 or auxiliar[1] <= mleves[-1][1]:

		mleves.append(auxiliar[:])


	array.append(auxiliar[:])
	auxiliar.clear()


for c in mleves:

	for v in mpesadas:

		if c[0] == v[0] and c[1] == v[1]:

			mleves.remove(c)
			mpesadas.remove(v)

print(f'''\nForam cadastradas {len(array)} pessoas
As pessoas mais pesadas foram {mpesadas[-2:]}
As pessoas mais leves foram {mleves[-2:]}''')
