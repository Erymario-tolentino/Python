# Crie um programa que leia dois valores e mostre um menu como o ao lado na tela:
# Seu programa devera realizar a operação solicitada em cada caso.
#  [ 1 ] somar
#  [ 2 ] multiplicar
#  [ 3 ] maior
#  [ 4 ] novos numeros
#  [ 5 ] sair do programa

from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opc = s = m = maior= 0
while opc != 5 :
    print('     [ 1 ] somar')
    print('     [ 2 ] multiplicar')
    print('     [ 3 ] maior')
    print('     [ 4 ] novos numeros')
    print('     [ 5 ] sair do programa')
    opc = int(input('>>>>> Qual e a sua opção? '))
    if opc == 1 :
        s = n1 + n2
        print('A soma entre {} e {} e {}'.format(n1 , n2 , s))
    elif opc == 2 :
        m = n1 * n2
        print('O resultado de {} x {} e {}'.format(n1 , n2 , m))
    elif opc == 3 :
        if n1 > n2 :
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor e {}'.format(n1 , n2 , maior))
    elif opc == 4 :
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opc == 5 :
        print('Finalizando...')
    else:
        print('Opção invalida. Tente novamente')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')
