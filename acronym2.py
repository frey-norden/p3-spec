stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"
sentList = sent.split()
acro = ''
for wrd in sentList:
    if wrd not in stopwords:
        acro += wrd[:2]+'. '

acro = acro[:-2].upper()

print(acro)
