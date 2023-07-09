# Crie um programa que leia varios numeros inteiros pelo teclado.No final da execução, mostre a media entre todos os valores e qual foi o maior e menor valores lidos. O Programa deve perguntar ao usuario se ele quer ou não continuar a digitar valores.

soma = quant = media = maior = menor = 0
r = 'S'
while r == 'S' :
    num = int(input('Digite um numero: '))
    soma += num
    quant += 1
    if quant == 1 :
        maior = menor = num
    else:
        if num > maior :
            maior = num
        elif num < menor :
            menor = num
    r = str(input('Quer continuar? ')).strip().upper()
media = soma / quant
print('Voce digitou {} numeros e a media foi {:.2f}'.format(quant , media))
print('O maior valor foi {} e o menor foi {}'.format(maior , menor ))