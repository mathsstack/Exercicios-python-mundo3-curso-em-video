from datetime import date

def voto(ano_de_nascimento):
    
    idade = date.today().year - ano_de_nascimento
    
    if idade >= 18 and idade < 65:
        return "Voto obrigatório"
    if idade >= 65:
        return "Voto opcional"
    else:
        return "Voto negado"
    
ano_de_nascimento = int(input("Digite o ano de nascimento: "))    
print(voto(ano_de_nascimento))
