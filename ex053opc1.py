# Crie um programa que leia uma frase qualquer e diga se ela e um palindromo, desconsiderando os espaços. 
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1 , - 1 , - 1):
    inverso += junto[letra]
print('O inverso de {} e {}'.format(junto , inverso))
if inverso == junto :
    print('Temos um palidromo!')
else:
    print('A frase digitada não e um palidromo!')
