from datetime import date

current_year = date.today().year

trabalhador = {
    
    "nome": "",
    "idade": 0,
    "carteira_de_trabalho": 0
}

trabalhador["nome"] = str(input("Digite o nome: "))
ano_de_nascimento = int(input("Digite o ano de nascimento"))
trabalhador["idade"] = current_year - ano_de_nascimento
trabalhador["carteira_de_trabalho"] = int(input("Digite a carteira de trabalho: "))

if trabalhador["carteira_de_trabalho"] != 0:
    
    trabalhador["ano_de_contratacao"] = int(input("Digite o ano de contracação: "))
    trabalhador["salario"] = float(input("Digite o salário: R$ "))
    trabalhador["idade_aposentadoria"] = trabalhador["ano_de_contratacao"] + 35
    
 
 
print('-=' * 20)

for k, v in trabalhador.items():
    
    print(f'{k} tem valor {v}')
    
print('-=' * 20)
