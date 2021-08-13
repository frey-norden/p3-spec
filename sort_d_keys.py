L = ['E', 'F', 'B', 'M', 'C', 'X', 'X', 'X', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D', 'B', 'M', 'C', 'X', 'X', 'X', 'A', 'D', 'I', 'I', 'C', 'B', 'A']

d = {}
for x in L:
    if x in d:
        d[x] += 1
    else:
        d[x] = 1

y = sorted(d.keys())

for k in y:
    print('{} appears {} times in this list'.format(k, d[k]))
