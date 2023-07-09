# Refaça o DESAFIO 009, mostrando a tabuada de um numero que o usuario escolher, so que agora utilizando um laço for.
tab = int(input('Digite um numero para ver sua tabuada: '))
for c in range(0 , 11):
    m = tab * c
    print('{} x {} = {}'.format(tab , c , m))