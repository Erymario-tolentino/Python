# Faça um programa que leia o sexo de uma pessoa, mas so aceite os valores 'M' ou 'F'.Caso esteja errado, peça a digitação novamente ate ter um valor correto.
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()
while sexo not in 'MmFf' :
    sexo = str(input('Dados invalidos. Por Favor, informe seu sexo: ')).strip().upper()
print('Sexo {} registrado com sucesso'.format(sexo))
