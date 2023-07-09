# Desenvolva um programa que leia o comprimeto de tres retas e diga ap usuario se elas posem ou não formar um triangulo.
print('-=' * 20)
print('Analisando de triangulos')
print('-=' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceira segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Os segmetos acima PODEM FORMAR UM TRIANGULO!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR UM TRIANGULO')