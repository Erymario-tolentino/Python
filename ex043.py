# Desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# -Abaixo do 18.5: Abaixo do peso
# -Entre 18.5 e 25: Peso ideal
# -25 ate 30: Sobrepeso
# -30 ate 40: Obesidade
# -Acima de 40: Obesidade mmorbida  

peso = float(input('Qual e seu peso? (KG) '))
altura = float(input('Qual e sua altura? (M) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa e de {:.1f}'.format(imc))
if imc < 18.5 :
    print('Voce esta ABAIXO do PESO NORMAL')
elif 18.5 <= imc < 25 :
    print('PARABENS, voce esta na faixa se PESO NORMAL')
elif 25 <= imc < 30 :
    print('Voce esta em SOBREPESO')
elif 30 < imc < 40 :
    print('Voce esta em OBESIDADE, cuidado!')
elif imc >= 40:
    print('Voce esta em OBESIDADE MORBIDA, cuidado!')
