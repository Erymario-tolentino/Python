# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiusculas e minusculas.
# Quantos letras ao todo (sem considerar espaços).
# quantos letras tem primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
divido = nome.split()
print('Seu nome maisculas e {}'.format(nome.upper()))
print('Seu nome minusculas e {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome {} e ele tem {} letras'.format(divido[0] , len(divido[0])))