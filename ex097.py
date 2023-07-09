# Faça um programa que tenha uma função chamado escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
# EX: escreva('Olá, mundo!')

def escreva(msg) :
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


# programa principal
escreva('Olá, mundo!')
escreva('Aprenda programar condigo de python')
escreva('Cev')
