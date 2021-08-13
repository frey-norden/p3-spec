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
def g(k):
    return d[k]

y = sorted(d.keys(), key=g, reverse=True)

# loop through them keys playa
for key in y:
    print('{} appears {} times'.format(key, d[key]))
