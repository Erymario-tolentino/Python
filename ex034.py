# Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu amento.
# Para salario superiores a R$1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento e de 15%.

salario = float(input('Qual e o salario do funcionario? R$ '))
if salario <= 1250:
    novo = salario + (salario * 15 /100)
else:
    novo = salario + (salario * 10 /100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario , novo))
