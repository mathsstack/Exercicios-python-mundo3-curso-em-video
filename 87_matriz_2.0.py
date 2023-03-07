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


somapares = 0
somacolunatres = 0

for c in matriz:
	for p, v in enumerate(c):

		if v % 2 == 0:
			somapares+=v

		if p == 2:
			somacolunatres += v

		print(f'[ {v} ] ', end="")

	print('\n')


print(f'''\nA soma dos valores pares é {somapares}
A soma dos valores da coluna 3 é {somacolunatres}
O maior valor da segunda linha é {sorted(matriz[1])[-1]}
''')
