import moeda

num = int(input("Type a number: "))
dobro = moeda.dobrar(num)

print(f'''
The double of the {moeda.moeda(num)} is {moeda.moeda(dobro)}''')
