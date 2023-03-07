v1 = int(input('Digite um valor: '))
v2 = int(input('Digite outro valor: '))
v3 = int(input('Digite outro valor: '))
v4 = int(input('Digite outro valor: '))

values = (

v1, v2, v3, v4

)

pares = 0
three = 0

for p, c in enumerate(values):

	if c % 2 == 0:
		pares+=1

	if c == 3:
		three = 1

print(f'''\nO valor 9 apareceu {values.count(9)} vezes
Foram digitados {pares} numeros pares''')

if three == 0:
	print('O numero 3 nao foi digitado nemhuma vez')
else:
	print(f'O 1° numero 3 esta na {values.index(3) + 1}° posicao')

