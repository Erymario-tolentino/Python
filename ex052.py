# Faça um programa que leia um numero inteiro e diga se ele e ou não um numero primo.
tot = 0
num =int(input('Digite um numero: '))
for c in range( 1 , num + 1):
    if num % c == 0:
        print('\033[33m]' , end=' ')
        tot +=1
    else:
        print('\033[31m]' , end=' ')
    print('{}'.format(c) , end=' ')
print ('\nO numero {} foi divisivel {} vezes'.format(num , tot ))
if tot == 2:
    print('E por isso ele e PRIMO!')
else:
    print('E por NãO E PRIMO!')
    