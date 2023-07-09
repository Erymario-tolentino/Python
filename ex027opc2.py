# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
# Ex: Ana Maria de Souza
# primeiro = Ana
# ultimo = Souza
nome = str(input('Digite seu nome completo: '))
print('Muito prazer em te conhecer!')
divido = nome.split()
print('Seu primeiro nome e {}'.format(divido[0]))
print('Seu ultimo nome e {}'.format(divido[len(divido)-1]))