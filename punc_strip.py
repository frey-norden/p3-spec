

def punctuation_stripper(s):
    ''' takes a string s and strips the puncs
        returns a new string of only letters '''

    punctuation = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    # punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
    # alternative is list above: punctuation_chars  --> both work based on preference

    new_string = ''

    for letter in s:
        if letter not in punctuation:
            new_string += letter

    return new_string

def get_pos(s):
    ''' takes a string s and determines if positive connotation
        returns  a positive int for how many words are +
     '''
     s.lower()
     wrds = s.split()



     # list of positive words to use
     positive_words = []
     with open("positive_words.txt") as pos_f:
         for lin in pos_f:
             if lin[0] != ';' and lin[0] != '\n':
                 positive_words.append(lin.strip())

     if s in pos_f:
