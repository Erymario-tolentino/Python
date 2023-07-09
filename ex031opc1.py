# Desenvolva um programa que pergunte a distancia de uma viagem em KM. Calcule o preço da passagem, cobrando R$0,50 por km para viagens de ate 200Km e R$0,45 para viagens mais longas.

distancia = float(input('Qual e a distancia da sua viagem? '))
print('voce esta prestes a começar uma viagem de {:.2f}Km.'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('E o preço da sia passagem sera R${:.2f} '.format(preço))