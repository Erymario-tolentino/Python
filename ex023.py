# Faça um programa que leia um numero de 0 a 9999 e mostre tela
# Ex: Digite um numero:1834
# Unidade:4 dezena:3 centena:8 milhar:1
num = int(input('Informe um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o numero {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('milhar: {}'.format(m))