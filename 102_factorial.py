from time import sleep

def fatorial(numero, show=False):
    
    """
    Displays a factorial of a number:
    
    numero: number to be calculated
    show: boolean argument that shows the calculating process if it is enabled
    """
    
    f = 1
    
    print(f'Calculating fatorial of {numero}...\n' if show == True else '')
    while numero > 0:
        f *= numero;
        print(numero if show == True else '')
        print('x' if show == True else '')
        numero -= 1
     
    print('=' if show==True else '')   
    return f

num = int(input('Type a number: '))    
print(fatorial(num, True))
help(fatorial)
