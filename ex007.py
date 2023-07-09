#  Desenvolva um programa que leia as duas notaas de um aluno, calcule e mostre a sua media.
nota1 = float(input('Primeiro nota do aluno: '))
nota2 = float(input('Segundo nota do aluno: '))
media = (nota1 + nota2) /2
print('A media entre {:1f} e {:1f} e igual a {:1f}'.format(nota1 , nota2 , media))