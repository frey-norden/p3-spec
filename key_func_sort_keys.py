# here is a list, insert your own if u want
L = ['E', 'F', 'B', 'M', 'C', 'X', 'X', 'X', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D', 'BB', 'M', 'C', 'X', 'X', 'X', 'A', 'D', 'I', 'I', 'C', 'B', 'A']

# here is the dictionary freq counter

d = {}
for x in L:
    if x in d:
        d[x] += 1
    else:
        d[x] = 1

# a func to feed keys w/ a key func - aka keys to yo func
# hopefully we can funk up yo databanks

# loop and sort through them keys simultaneously playa
for key in sorted(d, key=lambda key: d[key], reverse=True):
    print('{} appears {} times'.format(key, d[key]))
