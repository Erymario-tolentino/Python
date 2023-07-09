# Crie um programa que vai ler varios numeros e colocar e colocar em uma lista. Depois disso, Crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente. Ao final, mostre o conteudo das tres listas geradas.

num = list()
pares = list()
impares = list()
while True :
    num.append( int(input('Digite um numero: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn' :
        break
for i , v in enumerate(num) :
    if v % 2 == 0 :
        pares.append(v)
    elif v % 2 == 1 :
        impares.append(v)
print('-=' * 30)
print(f'A lista completa e {num}')
print(f'A lista de pares e {pares}')
print(f'A lista de impares e {impares}')