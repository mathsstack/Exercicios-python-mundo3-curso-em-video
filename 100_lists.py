from random import randint
from time import sleep

numeros = list() 

def sorteia(lista):
    
    print('Sorteando 5 valores: ')
    for c in range(0, 5):
        lista.append(randint(0, 10))
        print(lista[c])
        sleep(0.5)
    
def soma_par(lista):
    
    soma = 0
    
    for c in lista:
        if c % 2 == 0:
            soma += c
            
    print(f'A soma dos pares é {soma}')
    
sorteia(numeros)    
soma_par(numeros)
    
