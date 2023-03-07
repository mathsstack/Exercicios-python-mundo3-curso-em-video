lista = []

while True:

	while True:
		valor = int(input('\nDigite um número: '))

		if valor in lista:
			print('\nO valor já existe!\n')
		else:
			lista.append(valor)
			print('\nAdicionado!\n')
			break

	while True:

		quer = input('Quer continuar [S/N]? ').strip().upper()

		if quer == 'N' or quer == 'S':
			break
		else:
			print('Invalid input')

	if quer == 'N':
		break

print('\n','-='*20)
print(f'\nValores crescentes: {sorted(lista)}')
