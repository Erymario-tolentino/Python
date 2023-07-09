# escreva um programa que leia um valor em metros e a exiba convertida
medida = float(input('Uma distancia em metros: '))
cm = medida * 100
mm = medida *1000
print('A medida de {}m corresponde a {}cm e {}mm'.format(medida , cm , mm))