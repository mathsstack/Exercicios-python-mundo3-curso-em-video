from random import randint
from time import sleep

print('-='*11)
print('\n   SORTEIO MEGA SENA   \n')
print('-='*11)

listaJogos = []

tempJogo = []

qtde = int(input('Quantos jogos quer gerar? '))

for c in range(0, qtde):

	for n in range(0, 6):

		tempJogo.append(randint(0, 60))

	listaJogos.append(sorted(tempJogo[:]))
	tempJogo.clear()


print('\nLista de jogos: \n ')
sleep(1)

for n, j in enumerate(listaJogos):

	print(f'Jogo {n}: {j}')
	sleep(1)

print('\nBOA SORTE!\n')
