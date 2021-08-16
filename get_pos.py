def strip_punctuation(s):
    ''' takes a string s and strips the puncs
        returns a new string of only letters '''

    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

    new_string = ''

    for letter in s:
        if letter not in punctuation_chars:
            new_string += letter

    return new_string

def get_pos(s):
    st = s.lower()
    clean_wrds = []
    wrds = st.split()
    for w in wrds:
        clean_wrds.append(strip_punctuation(w))
    print(clean_wrds)
    count = 0
    # list of positive words to use
    positive_words = ['wonderful', 'incredible']
    with open("positive_words.txt") as pos_f:
        for lin in pos_f:
            if lin[0] != ';' and lin[0] != '\n':
                positive_words.append(lin.strip())

    for w in clean_wrds:
        if w in positive_words:
            count += 1

    return count

test_string1 = 'Testing "what a truly wonderful day it is today! #incredible"'
test_string2 = 'what a truly Wonderful day it is today! #incredible'

print(get_pos(test_string1))
print(get_pos(test_string2))
