# Crie um programa onde o usuario digite uma expressão qualquer que use parenteses.Seu aplicativo devera analisar se a expressão passada esta com os parenteses abertas e fechados na ordem correta.

expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr :
    if simb == '(' :
        pilha.append('(')
    elif simb == ')' :
        if len(pilha) > 0 :
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0 :
    print('Sua expressão esta valida!')
else:
    print('Sua expressão esta errada!')
