# Crie um programa que leia um numero inteiro e mostre na tela se ele PAR ou IMPAR
num = int(input('Me diga numero qualquer: ')) 
if num % 2 ==0:
    print('O numero {} e PAR'.format(num))
else:
    print('O numero {} e IMPAR'.format(num))
