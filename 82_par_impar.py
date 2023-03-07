lista = []
lista_par = []
lista_impar = []

quer = 'S'

while quer == 'S':

	lista.append(int(input('\nDigite um valor: ')))

	while True:

		v = input('\nQuer adicionar mais valores[S/N]? ').strip().upper()

		if v != 'N' and v != 'S':
			print('Invalid')
		else:
			quer = v
			break

for c in lista:

	if c % 2 == 0:
		lista_par.append(c)
	else:
		lista_impar.append(c)


print(f'''\nLista geral: {lista}
Números pares: {lista_par}
Números ímpares: {lista_impar}''')
