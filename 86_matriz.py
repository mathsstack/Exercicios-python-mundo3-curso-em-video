matriz = [

[],
[],
[]

]

auxiliar = []

for c in range(0, 9):

	auxiliar.append(int(input('Digite um valor: ')))


index = 0

for c in matriz:

	for v in range(0, 3):

		c.append(auxiliar[index])
		index += 1

print('\n\nMatriz: \n\n')

for c in matriz:
	for v in c:

		print(f'[ {v} ] ', end="")

	print('\n')
