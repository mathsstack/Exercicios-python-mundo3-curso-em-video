classificacao = (

"Real Madrid",
"Barcelona",
"FC Bayern",
"Borussia Dortmund",
"Liverpool",
"Paris saint Germain",
"Arsenal",
"Manchester United",
"Manchester City",
"Chelsea"

)

print('5 primeiros classificados: \n')

for c in range(1, 6):

	print(f'{c}° -------------- {classificacao[c-1]}')

print('\nOs ultimos colocados: \n')

for c in range(0, -5, -1):

	print(f'{len(classificacao) + c}° -------------- {classificacao[-1 + c]}')

print('\nTimes em ordem alfabética: \n')

for c in sorted(classificacao):

	print(c)

for pos, time in enumerate(classificacao):

	if time == 'Paris saint Germain':

		print(f'\n{time} esta na {pos + 1}° posicao')
