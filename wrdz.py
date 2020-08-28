file = 'somefile.txt'
alist = []
with open(file, 'r') as f:
    lines = f.readlines()
    for line in lines:
        wrds = line.split()
        for wrd in wrds:
            if wrd not in alist:
                alist.append(wrd)

str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
freq_words = {}
wrds = str1.split()
for wrd in wrds:
    if wrd not in freq_words:
        freq_words[wrd] = 0
    freq_words[wrd] += 1
