p_phrase = "was it a car or a cat I saw"
r_phrase = ''

for s in range(1,len(p_phrase)+1):
    r_phrase += p_phrase[-s]

print(r_phrase)
