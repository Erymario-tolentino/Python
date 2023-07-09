# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dolares ela pode comprar.
real = float(input('Quanto dinheiro voce tem na carteira? R$'))
dolar = real / 3.27
print('com R${:.2f} voce pode comprar US${:.2f}'.format(real , dolar))