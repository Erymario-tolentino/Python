# Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:
# -O Primeiro valor e maior
# -O segundo valor e maior
# -Não existe valor maior, os dois são iguais 
n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
if n1 > n2:
    print('O PRIMEIRO valor e maior valor')
if n2 > n1:
    print('O SEGUNDO e maior valor')
else:
    print('Os dois valores são IGUAIS')