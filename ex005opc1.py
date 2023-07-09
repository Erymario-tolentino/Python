# Faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor.
num = int(input('Digite um numero: '))
ant = num - 1
suc = num + 1
print('Analisando o valor {}, seu antecessor e {} e o sucessor e {}'.format(num , ant , suc))