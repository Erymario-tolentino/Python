# Crie umm programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada, o programa devera perguntar se o usuario quer ou não continuar. No final, mostre:
# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantos mulheres tem menos de 20 anos.

tot18 = totH = totM20 = 0
while True :
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF' :
        sexo = str(input('Sexo: [M/F] ')).strip().upper()
    if idade >= 18 :
        tot18 += 1
    if sexo == 'M' :
        totH += 1
    if sexo == 'F' and idade < 20 :
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N' :
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos')
