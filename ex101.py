# Crie um programa que tenha uma função chamado voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
def voto(ano) :
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16 :
        return f'com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65 :
        return f'com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'com {idade} anos: VOTO OBRIGATÓRIO.'

nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))