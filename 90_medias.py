aluno = {}

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Média: '))

if aluno['media'] < 5:
    
    aluno['situacao'] = 'Reprovado'
else:
    aluno['situacao'] = 'Aprovado'
    

for k, v in aluno.items():
    
    print(f'{k}: {v}')
