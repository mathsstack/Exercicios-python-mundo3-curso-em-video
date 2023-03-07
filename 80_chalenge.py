lista = [50]

for c in range(0, 5):

	print(lista)
	valor = int(input('\nDigite um valor: '))

	maior = menor = lista[0]

	for c in lista:

		if c > maior:
			maior = c
		elif c < menor:
			menor = c

	if valor > maior:
		print('Added on last position')
		lista.append(valor)
	elif valor < menor:
		print('Added on first position')
		lista.insert(0, valor)
	else:

		index = 0
		minVal = menor

		for v, c in enumerate(lista):

			if c < valor and c > minVal:
				index = v
				minVal = c

		print(f'Added on position {index + 1}')
		lista.insert(index + 1, valor)

print(lista)
