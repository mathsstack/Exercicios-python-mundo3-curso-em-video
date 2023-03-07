lista = []

for c in range(0, 5):
	lista.append(int(input('Digite um número: ')))


maior = sorted(lista)[-1]
menor = sorted(lista)[0]

print(f'O maior valor digitado foi {maior} na posicao {lista.index(maior)} e o menor foi {menor} na posicao {lista.index(menor)}')
