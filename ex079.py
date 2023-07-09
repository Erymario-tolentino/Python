# Crie um programa onde o usuario possa digiar varios valores numericos e cadastre-os em uma lista.Caso numero o ja exista la dentro, ele não sera adicionado.No final,serão exibidos todos os valores unicos digitados, em ordem crescente.

numeros = list()
while True :
    n = int(input('Digite um valor: '))
    if n not in numeros :
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não voou adicionar...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn' :
        break
print('-=' * 30)
numeros.sort()
print(f'Voce digitou os valores {numeros}')
    