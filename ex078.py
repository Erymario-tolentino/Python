# Faça um programa que leia 5 valores numericas e guarde-os em uma lista. No final, mostre qual foi o maior e menor valores digitado e as suas respectivas posições na lista. 

listanum = []
mai = 0
men = 0
for c in range(0 , 5):
    listanum.append(int(input(f'Digitade um valor para a posição {c}: ')))
    if c == 0 :
        mai = men = listanum[c]
    else:
        if listanum[c] > mai :
            mai = listanum[c]
        if listanum[c] < men :
            men = listanum[c]
print('=-' * 30)
print(f'Voce digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ',end='')
for i , v in enumerate(listanum) :
    if v == mai :
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {men} nas posições ',end='')
for i , v in enumerate(listanum):
    if v == men :
        print(f'{i}...',end='')
print()
