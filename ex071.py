# Crie um programa que simule o funcionamento de um caixa eletronico. No inicio, pergunte ao usuario qual sera o valor a ser sacado (numero inteiro) e o programa vai informar quantas cedulas de cada valor serão entregues
# OBS: considere que a caixa possui cedulas de R$50, R$20 , R$10 e R$1.

print('=' * 30 )
print('----------' * 1 + ' BANCO CEV ' + '----------' * 1)
print('=' * 30)
valor = int(input('Que valor voce quer sacar? R$'))
total = valor
ced = 50
totCed = 0
while True :
    if total >= ced :
        total -= ced
        totCed += 1
    else:
        if totCed > 0 :
            print(f'Total de {totCed} celulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20 :
            ced = 10
        elif ced == 10 :
            ced = 1
        totCed = 0 
        if total == 0 :
            break
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')