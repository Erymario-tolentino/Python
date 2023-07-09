# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso , zero ate 20.
# Seu programa devera ler um numero pelo teclado(entre 0 e 20)

cont = ('zero' , 'um' , 'dois' , 'tres' , 'quatro', 'cinco' , 'seis' , 'sete' , 'oite' , 'nove' , 'dez' , 'onze' , 'doze' , 'treze' , 'catorze' , 'quize' , 'dezesseis' , 'dezessete' , 'dezoito' , 'dezenove' , 'vinte')
while True :
    num = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= num <= 20 :
        break
    print('Tente novamente. ',end='')
print(f'Voce digitou o numero {cont[num]}')