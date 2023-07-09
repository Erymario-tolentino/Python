# Crie um programa que leia nome a media de um aluno, guardando tambem a situação em um dicionario. No final, mostre o conteudo da estrutura na tela.

aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))
if aluno['media'] >= 7 :
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7 :
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-=' * 30)
for k , v in aluno.items() :
    print(f'{k} e igual a {v}')