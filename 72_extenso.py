lista_extenso = (

"zero",
"um",
"dois",
"três",
"quatro",
"cinco",
"seis",
"sete",
"oito",
"nove",
"dez",
"onze",
"doze",
"treze",
"quatorze",
"quinze",
"dezesseis",
"dezessete",
"dezoito",
"dezenove",
"vinte"

)

while True:

	numero = int(input('Type a number: '))

	if 0 <= numero <= 20:
		break
	print("\nInvalid number!")

print(f'\nVoce digitou o número {lista_extenso[numero]}');
