# Escreva um programa que leia numero inteiro qualquer e peça para o usuario escolher qual sera a base de conversão:
# - 1 para binario
# - 2 para octal
# - 3 para hexadecimal

num = int(input('Digite um numero inteiro: '))
print('Escolha uma das bases para conversão:')
print('[ 1 ] converter para BINARIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
opc = int(input('Sua opção: '))
if opc == 1:
    print('{} convertido para BINARIO e igual {}'.format(num , bin(num)[2:]))
elif opc == 2:
    print('{} convertido para OCTAL e igual {}'.format(num , oct(num)[2:]))
if opc == 3:
    print('{} convertido para HEXADECIMAL e igual {}'.format(num , hex(num)[2:]))
else:
    print('Opção invalido. Tente novamente')
