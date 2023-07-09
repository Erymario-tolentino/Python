# Crie uma tupla preenchida com os 20 primeiros colocados da tebela do campeonato Brasileira de Futebol, na ordem de colocação.Depois mostre:
# A) Os 5 primeiros.
# B) OS ultimos 4 colocados.
# C) Times em ordem alfabetica.
# D) Em que posição esta o time chapecoensa.

times = ('Corinthians' , 'Palmeiras' , 'Santos' , 'Gremio' , 'Cruzeiro' , 'Flamento' , 'Vasco' , 'Chapecoensa' , 'Atletico' , 'Potafogo' , 'Atletico-PR' , 'Bahia' , 'Sãõ paulo' , 'Fluminese' , 'Sport recife' , 'Ec vitoria' , 'Coritiba' , 'Avai' , 'Ponte Preta' , 'Atletico-GO' )
print('-=' * 15)
for t in times:
    print(t)
print('-=' * 15)
print(f'Os 5 primeiros são {times[0 : 5]}')
print('-=' * 15)
print(f'Os 4 ultimos são {times[ - 4:]}')
print('-=' * 15)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('-=' * 15)
print(f'O chapecoense esta na {times.index("Chapecoensa") + 1} posição')