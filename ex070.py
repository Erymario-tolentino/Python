# Crie um programa que leia o nome e o preço de varias produtos. O programa devera perguntar se o usuario vai continuar.No final, mostre:
# A) Qual e o total gasto na compra.
# b) Quantos produtos custam mais de R$1000.
# C) Qual e o nome do produto mais barato.
total = totmil = menor =  cont = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: ')).strip().upper()
    preço = float(input('Preço: R$'))
    cont += 1
    total += preço
    if preço > 1000 :
        totmil += 1
    if cont == 1 or preço < menor :
        menor = preço
        barato = produto
    resp =' '
    while resp not in 'SN' :
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N' :
        break
print('----------' * 2 + 'FIM DO PROGRAMA' + '----------' * 2)
print(f'O total da compra foi R${total:10.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000')
print(f'O produto mais barato custa R${menor:.2f}')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')