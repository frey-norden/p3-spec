stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"
orgList = org.split()
acro = ''
for wrd in orgList:
    if wrd not in stopwords:
        acro += wrd[0]
acro = acro.upper()
print(acro)
