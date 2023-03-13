def aumentar(value, qtde, formatar=False):
    
    return moeda(value + qtde) if formatar == True else value + qtde
    
def diminuir(value, qtde, formatar=False):
    
    return moeda(value - qtde) if formatar == True else value - qtde
    
def dobrar(value, formatar=False):
    
    return moeda(value * 2) if formatar == True else value * 2
    
def metade(value, formatar=False):
    
    return moeda(value / 2) if formatar == True else value / 2
    
def moeda(value):
    
    return 'R$ ' + str(value) + ',00'
