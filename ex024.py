# Crie um program que leia o nome de um cidade e gida se ela começa ou não com o nome "Santo"
cid = str(input('Em que cidade voce nasceu? ')).upper().strip()
print(cid[:5] == 'Santo'.upper())