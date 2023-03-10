def maior(num):
    
    maior = 0
    
    for p, c in enumerate(num):
        
        if p == 0: maior = c
        
        if c > maior: maior = c
        
    print(f'O maior valor é {maior}')


lista_valores = []

for c in range(0, 4):
    
    lista_valores.append(int(input("Type a value: ")))
    
maior(lista_valores)  
