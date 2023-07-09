# Escreva um programa que pergunta a quantidade de KM de percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.calculeo preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por KM rodando. 
dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos KM rodados?'))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar e de R${:.2f}'.format(pago))