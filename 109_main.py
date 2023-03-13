import moeda

num = int(input("Type a number: "))

print(f'''
The double of the {moeda.moeda(num)} is {moeda.dobrar(num, True)}''')
