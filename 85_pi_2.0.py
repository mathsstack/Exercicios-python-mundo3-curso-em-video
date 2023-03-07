lista = [

[],
[]

]

for c in range(0, 7):

	valor = int(input('Digite um valor: '))

	if valor % 2 == 0:

		lista[0].append(valor)
	else:
		lista[1].append(valor)


lista[0].sort()
lista[1].sort()

print(f'''\nLista completa: {lista}
Valores pares: {lista[0]}
Valores impares: {lista[1]}''')
