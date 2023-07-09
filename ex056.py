# Desenvolva um programa que leia o nome, idade e sexo de 4 pessos.No final do programa, mostre:
# A media de idade do grupo.
# Qual e o nome do homem mais velho.
# Quantas mulheres tem menos de 20 anos.
somaidade = 0
mediaidade = 0
MaiorIdadeHomem = 0
NomeVelho = ''
TotMulher20 = ''
for p in range( 1 , 5 ):
    print('-------- {}a PESSOA --------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    somaidade += idade
    if p == 1 and sexo in 'Mm' :
        MaiorIdadeHomem = idade
        NomeVelho = nome
    if  sexo in 'Mm' and idade > MaiorIdadeHomem :
        MaiorIdadeHomem = idade 
        NomeVelho = nome
    if sexo in 'Ff' and idade < 20 :
        TotMulher20 += 1
        

mediaidade = somaidade / 4
print('A media de idade do grupo e de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(MaiorIdadeHomem , NomeVelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(TotMulher20))