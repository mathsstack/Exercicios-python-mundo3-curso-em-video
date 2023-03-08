lista_pessoas =list()
pessoa = dict()

quer = 'S'
while quer == 'S':
    
    pessoa["nome"] = input("Digite um nome: ")
    pessoa["sexo"] = input("Escolha o sexo: [M/F] ").strip().upper()
    pessoa["idade"] = int(input("Digite a idade: "))
    lista_pessoas.append(pessoa.copy())

    while True:
        choice = input("Quer continuar? [S/N] ").strip().upper()
        
        if choice != 'S' and choice != 'N':
            print('Invalid')
        else:
            quer = choice
            break

#declarating variables 
media_idades = 0;
lista_mulheres = list()
lista_idade_maior_media = list()

#Calculating media
for c in lista_pessoas:
    media_idades += c["idade"]

media_idades /= len(lista_pessoas)

#Iteraing

for c in lista_pessoas:
    
    if c["sexo"] == 'F': lista_mulheres.append(c)
    if c["idade"] > media_idades: lista_idade_maior_media.append(c)

print('ESTATÍSTICA: \n')

print(f'Foram cadastradas {len(lista_pessoas)} pessoas')
print(f'A média de idade do grupo é {media_idades}')
print(f'As mulheres cadastradas foram: ')

for c in lista_mulheres:
    print(f'Nome: {c["nome"]}')
    
print(f'As pessoas com idade maior do que a média são: ')

for c in lista_idade_maior_media:
    
    print(f'Nome: {c["nome"]}, Idade: {c["idade"]}')
