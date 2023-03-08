lista_jogadores =list()

quer = 'S'
while quer == 'S':
    
    jogador = dict()
    gols = list()
    
    jogador["nome"] = input("Digite um nome: ")
    qtde_partidas = int(input("Quantas partidas jogou? "))
    
    for c in range(1, qtde_partidas + 1):
        gols.append(int(input(f"Quantos gols na partida {c}? ")))
    jogador["gols"] = gols[:]
    
    total_de_gols = 0
    for c in gols:
        total_de_gols += c
    jogador["total_de_gols"] = total_de_gols
    
    lista_jogadores.append(jogador.copy())

    while True:
        choice = input("Quer continuar? [S/N] ").strip().upper()
        
        if choice != 'S' and choice != 'N':
            print('Invalid')
        else:
            quer = choice
            break

print('-=' * 20)

print("Posicao      Nome:       Total de gols:")
for p, c in enumerate(lista_jogadores):
    print(f'{p}         {c["nome"]}          {c["total_de_gols"]}')
    
print('-=' * 20)

while True:
    
    choice = int(input("Mostrar dados de qual jogador? (999 para)"))
    
    if choice == 999: break
    
    for p, c in enumerate(lista_jogadores[choice]["gols"]):
        
        print(f'Na partida {p + 1} fez {c} gols')
