# Faça o DESAFIO 035 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo sera formado:
# -Equilatero: todos os lados iguais
# -Isosceles: dois lados iguais
# -Escaleno: todos os lados diferentes

print('-=' * 20)
print('Analisando de triangulos')
print('-=' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceira segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Os segmetos acima PODEM FORMAR UM TRIANGULO!',end=' ')
    if r1 == r2 == r3 :
        print('Equilatero!')
    elif r1 != r2 != r3 !=r1 :
        print('ESCALENO!')
    else:
        print('ISOSCELES')
else:
    print('Os segmentos acima NÃO PODEM FORMAR UM TRIANGULO')