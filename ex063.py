# Escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequencia de Fibonacci.
# EX: 0 => 1 => 2 => 5 => 8
print('-' * 30)
print('Sequencia de Fibonacci')
print('-' * 30)
n = int(input('Quantos termo voce quer mostrar? '))
t1 = 0
t2 = 1
print('-' * 30)
print('{} => {}'.format(t1 , t2 ),end='')
cont = 3
while cont <= n :
    t3 = t1 + t2
    print(' => {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print('=> FIM')
print('-' * 30)
