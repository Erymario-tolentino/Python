# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - A vista dinheiro/cheque: 10% de desconto
# - A vista no cartão: 5% de desconto
# - Em ate 2x no cartão : preço normal
# - 3x ou mais no cartão: 20% de juros
print('='*15, 'LOJAS ERYMARIO', '='*15)
preço = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] a vista dinheiro/cheque')
print('[ 2 ] a vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x no cartão')
opc =int(input('Qual e a opção: '))
if opc == 1 :
    total = preço - (preço * 10 /100)
elif opc == 2 :
    total = preço - (preço * 5 / 100)
elif opc == 3 :
    total = preço
    parcela = total / 2
    print('Sua compra sera parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opc == 4 :
    total = preço + (preço * 20 / 100) 
    totparc = int(input('Quantos parcelas?'  ))
    parcela = total / totparc
    print('Sua conta sera parcelada em {}x de R${:.2f} COM JUROS'.format(totparc , parcela))
else:
    total = preço
    print('OPCÃO INVALIDO DE PAGAMENTO. TENTE NOVAMENTO')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço , total ))