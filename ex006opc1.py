# crie um algoritmo que leia  um numero e mostre o seu dobro , triplo , raiz quadrada
num = int(input('Digite um numero: '))
d = num * 2
t = num * 3
r = num **(1/2)
print('O dobro de {} vale {}.'.format(num , d))
print('O triplo de {} vale {}.'.format(num , t))
print('A raiz quadrada de {} e igual a {:2f}.'.format(num , r))