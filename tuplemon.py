
lst_tups = [('Articuno', 'Moltres', 'Zaptos'), ('Beedrill', 'Metapod', 'Charizard', 'Venasaur', 'Squirtle'), ('Oddish', 'Poliwag', 'Diglett', 'Bellsprout'), ('Ponyta', "Farfetch'd", "Tauros", 'Dragonite'), ('Hoothoot', 'Chikorita', 'Lanturn', 'Flaaffy', 'Unown', 'Teddiursa', 'Phanpy'), ('Loudred', 'Volbeat', 'Wailord', 'Seviper', 'Sealeo')]
t_check = []
for ea in lst_tups:
    t_check.append(ea[2])

print(t_check)

d = {'k1': 3, 'k2': 7, 'k3': 'some other value'}

for k, v in d.items():
    #k = p[0]
    #v = p[1]
    print('key: {}, value: {}'.format(k, v))

pokemon = {'Rattata': 19, 'Machop': 66, 'Seel': 86, 'Volbeat': 86, 'Solrock': 126}
p_names, p_number = [], []
items = pokemon.items()
# this loads up the lists w keys and values from above dictionary
for k, v in items:
    p_names.append(k)
    p_number.append(v)
