# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = str(input('Qual e seu nome completo? ')).strip().upper()
print('Seu nome tem Silva? {}'.format('SILVA' in nome))