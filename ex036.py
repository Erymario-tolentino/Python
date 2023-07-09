# Escreva um programa para aprovar o emprestimo bancario paara a compra de uma casa.Pergunte p valor da casa, o salario do comprador e em quantos anos ele vai pagar.
# A prestação mensal, não pode exceder 30% do salario ou então o emprestimo sera negado.

casa = float(input('Valor da casa: R$ '))
salario = float(input('Salario do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar um casa de R${:.2f} em casa em {} anos'.format(casa , anos), end='')
print(' a prestação sera de R$ {:.2f}'.format(prestação))
if prestação <= minimo :
    print('Emprestimo pode ser CONDECINDO')
else:
    print('Emprestimo NEGADO')