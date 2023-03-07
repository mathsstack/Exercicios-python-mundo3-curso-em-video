lista = []

quer = 'S'

while quer == 'S':

	lista.append(int(input('\nDigite um número: ')))

	while True:

		variable = input('\nQuer continuar? ').strip().upper()

		if variable != 'N' and  variable != 'S':
			print('\nInvalid input')
		else:
			quer = variable
			break


print(f'''\nForam digitados {len(lista)} números
Os valores em ordem crescente sao: {sorted(lista)}''')

if 5 in lista:
	print('O valor 5 foi digitado na lista')
else:
	print('O valor 5 nao foi digitado nenhuma vez')

