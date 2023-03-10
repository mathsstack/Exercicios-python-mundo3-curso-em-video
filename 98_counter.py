from time import sleep

def contador(inicio, fim, passo):
    
    if passo == 0: passo = 1
    if passo < 0: passo *= -1
    
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
    
    compenser = 1
    if inicio > fim:
        passo *= -1
        compenser = -1
        
    for c in range(inicio, fim + compenser, passo):
        print(c)
        sleep(0.3)  
        
    print('\nFIM')
   
   
contador(1, 10, 1)
contador(10, 0, 2)   

print('Agora é a sua vez: ')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)
