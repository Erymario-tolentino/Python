# Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares.Se o valor digitado for impar, desconsidere-o
soma = 0
cont = 0
for c in range(1 , 7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0 :
        soma += c
        cont += 1
print('Voce informou {} numeros PARES e a soma foi {}'.format(cont , soma))