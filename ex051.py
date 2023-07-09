# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
primerio = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
decimo = primerio + (10 - 1 ) * razão
for c in range( primerio , decimo , razão):
    print('{}'.format(c), end=' ->')
print(' ACABOU')
