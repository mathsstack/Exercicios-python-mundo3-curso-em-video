expressao = input('Digite a expressao: ').strip()

openP = expressao.count('(')
closeP = expressao.count(')')

if openP == closeP:

	print('\nA expressao esta correta')

elif openP > closeP:

	print(f'\nA expressao esta errada. Voce abriu {openP - closeP} parenteses a mais')
else:
	print(f'\nA expressao esta errada. Voce fechou {closeP - openP} parenteses a mais')

