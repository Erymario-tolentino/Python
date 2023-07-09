# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h,mostre uma mensagem diendo que ele foi multado
# dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada km acima do limite.

velocidade = int(input('Qual e a velocidade atual do carro? '))
if velocidade >= 80:
    print('MULTADO! Voce excedeu o limite permitido que e de 80km/h \nVoce deve pagar um multa de R$280.00!')
    multa = (velocidade - 80) * 7
    print('Voce deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')