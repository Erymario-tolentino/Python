# Faça um algoritmo que leia o preço de um porduto e mostre seu novo preço de um produto e mostre seu novo preço, com 5% de desconte
preço = float(input('Qual e o preço do produto? R$'))
desc = preço-(preço * 5 /100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preço , desc))