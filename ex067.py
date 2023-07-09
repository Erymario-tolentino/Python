# Faça um programa que mostre a tabuada de varios numeros, um de cada vez, para cada valor digitado pelo usuario. O programa sera interrompido quando o numero solicitado for negativo. 

cont = 0
while True :
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30 )
    if n < 0:
        break
    for c in range(1 , 11):
        print(f'{n} x {c} = { n * c }')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRANDO. volte sempre!')