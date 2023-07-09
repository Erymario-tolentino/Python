# Crie um programa que leia varios numeros inteiros pelo teclado.O programa so vai parar quando o usuario digitar o valor 999, que e a condição de parada.No final, mostre quantos numeros foram digitados e qual a soma entre eles (desconsiderando o flag). 

s = quant = 0
while True :
    n = int(input('Digite um valor (999 para parar):'))
    if n == 999 :
        break
    s += n
    quant +=1
print(f'A soma dos {quant} valores foi {s}')