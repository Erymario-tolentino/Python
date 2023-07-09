# Crie um programa que vai ler varios numeros e colocar em uma lista. Depois disso, mostre:
# A) Quantos numeros foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e esta ou não na lista.

valores = []
while True :
    valores.append( int(input('Digite um valores: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn' :
        break
print('-=' * 30)
valores.sort(reverse=True)
print(f'Os valores em ordem descrescente são {valores}')
if 5 in valores :
    print('O valor 5 faz parte da lisa!')
else:
    print('O valor 5 não foi encontrado na lista')