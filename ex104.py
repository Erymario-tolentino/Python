# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do python, só que fazendo a validação para aceitar apenas um valor numérica      EX: n = leiaInt(' Digite um n ')

def leiaInt(msg) :
    ok = False
    valor = 0
    while True :
        n = str(input(msg))
        if n.isnumeric() :
            valor = int(n)
        else:
            print(f'ERRO! digite um número inteiro válido.')
        if ok :
            break
        return valor


# programa principal
n = leiaInt('Digite um número: ')
print(f'você acabou de digitar o númerico {n}')