# Crie um program que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem no final, de acordo com a media atiginda:
# Media abaixo de 5.0: REPROVADO
# Media entre 5.0 e 6.9: RECUPERAÇÃO
# Media 7.0 ou superior: APROVADO
n1 = float(input('Primeiro nota: '))
n2 = float(input('Segundo: '))
media = (n1 + n2 ) / 2
print('Tirando {:.1f} e {:.1f}, a media do aluno e {} '.format(n1 , n2 , media))
if media >= 5 and media < 7 :
    print('O aluno esta de RECUPERAÇÃO.')
elif media >= 7:
    print('O aluno esta APROVADO.')
else:
    print('O aluno esta REPROVADO.')
