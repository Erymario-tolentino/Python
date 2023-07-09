# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um numero de tipo inválido. Aproveite e crie também uma função leiaFloaat() com a mesma funcionalidade.

def leiaInt(msg) :
    while True :
        try:
            n = int(input(msg))
        except (ValueError , TypeError) :
            print('ERRO: por favor, digite um número intero válido.')
            continue
        except (KeyboardInterrupt) :
            print('Usuário preferiu não digitar esse número.')
            return 0
        else:
            return n

        
def leiaFloat(msg) :
    while True :
        try:
            n = float(input(msg))
        except (ValueError , TypeError) :
            print('ERRO: por favor, digite um número intero válido.')
            continue
        except (KeyboardInterrupt) :
            print('Usuário preferiu não digitar esse número.')
            return 0
        else:
            return n


n1 = leiaInt('Digite um Inteiro: ')
n2 = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')
 