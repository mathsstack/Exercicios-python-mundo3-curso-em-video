jogador = dict()

jogador["nome"] = str(input("Digite o nome do jogador: "))
jogador["numero_de_partidas"] = int(input("Quantas partidas jogou? "))

gols = list()

for c in range(1, jogador["numero_de_partidas"] + 1):
    
    gols.append(int(input(f"Quantos gols na partida {c}? ")))
    

total_de_gols = 0
for c in gols:
    total_de_gols += c
    
jogador["gols"] = gols
jogador["total_de_gols"] = total_de_gols

print('-=' * 20)
for k, v in jogador.items():
    
    if k == "numero_de_partidas": continue
    print(f'{k} tem valor {v}')
    
print('\n')

for p, c in enumerate(gols):
    
    print(f'Na partida {p + 1}, fez {c} gols')
    
print('-=' * 20)
