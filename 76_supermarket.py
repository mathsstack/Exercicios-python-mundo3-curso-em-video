products = (

"Arroz", 5.00,
"Feijao", 10.00,
"Mortadela", 6.00,
"Cheiro verde", 2.00,
"Batata", 2.00

)

print('Listagem de produtos: \n')

for product in range(0, 10, 2):

	print(products[product], '-' * (20 - len(products[product])) + 'R$ ', products[product + 1])
