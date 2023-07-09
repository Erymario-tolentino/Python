# Crie pequeno sistema modularizado que permite cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
# O sistema só vai ter 2 opcões: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.

from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not  arquivoExiste(arq) :
    criarArquivo(arq)
 

while True :
    resposta = menu(['Ver pessoas cadastrada' , 'Cadastradas nova pessoa' , 'sair do sistema'])
    if resposta == 1 :
        lerArquivo('cursoemvideo.txt')
    elif resposta == 2 :
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade ')
        cadastrar(arq , nome , idade)
    elif resposta == 3 :
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        ('ERRO! digite um opção válida!')
    sleep(2)