alunos = []
aluno = []
notas = []

for c in range(0, 3):

	nome = input('\nNome: ').strip()
	n1 = float(input('Primeira nota: '))
	n2 = float(input('Segunda nota: '))

	notas.append(n1)
	notas.append(n2)

	aluno.append(nome[:])
	aluno.append(notas[:])

	alunos.append(aluno[:])

	notas.clear()
	aluno.clear()

print('-='*10)
print('\nIndice         Nome           Media')
print('-'*20)

for i, aluno in enumerate(alunos):

	media = (aluno[1][0] + aluno[1][1]) / 2

	print(f'{i}         {aluno[0]}        {media}')

print('-'*20)

while True:

	choice = int(input('\nMostrar notas de qual aluno (999 interrompe)? '))

	if choice == 999:
		break

	print(f'Nome: {alunos[choice][0]} Notas: {alunos[choice][1]}')



