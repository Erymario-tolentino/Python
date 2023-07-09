# Faça um programa que tenha uma função chamada área(), que receba dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def área(larg , comp) :
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m@.')



# programa principal
print('controle de Terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l , c)