from random import randint
from time import sleep

#sortear os dados

jogadores = {}
numeros_jogados = list()

while len(numeros_jogados) < 4:

    n = randint(1, 6)
    tem = False
    
    for v, c in enumerate(numeros_jogados):
        if str(n) in str(numeros_jogados[v]):
            tem = True
            
    if tem == False:
        
        numeros_jogados.append(n)
        jogadores[f'jogador{len(numeros_jogados)}'] = n
        print(f'Jogador {len(numeros_jogados)}: ', end='')
        print(jogadores[f'jogador{len(numeros_jogados)}'])
    
        sleep(1)
    else:
        continue
    
#ordenar o dicionario   

lista_valores = list()    
lista_ordenada = list()
dicionario_ordenado = dict()

for c in jogadores.values():
    lista_ordenada.append(c)
    lista_valores.append(c)
    
lista_ordenada = sorted(lista_ordenada)    
    
for v in range(len(lista_ordenada) - 1, -1, -1):
    for c in lista_valores:
        
        if lista_ordenada[v] == c:
            dicionario_ordenado[f'jogador{lista_valores.index(c) + 1}'] = c

#imprime a lista:
        
print('\n*****Classificação******\n')

for k in dicionario_ordenado:
    
    print(f'{k}: ', end='')
    print(dicionario_ordenado[k])
