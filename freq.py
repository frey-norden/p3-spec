def most_common_letter(s):
    ''' Take a string s and returns most_common_letter'''
    if type(s) == str or type(s) == list:
        frequencies = freq_Count(s)
    else:
        frequencies = letterCount(s)
    return best_key(frequencies)

def freq_Count(sequence):
    ''' Counts frequencies of chars or item in sequence.
        Takes a string or list as input.
        Returns histogram dictionary.'''
    d = {}
    for c in sequence:
        if c not in d:
            d[c] = 0
        d[c] += 1
    return d

def best_key(dictionary):
    ''' Takes a dictionary arg and returns key with
        highest value.'''
    ks = dictionary.keys()    # get the key from dictionary
    top_one_now = list(ks)[0]  # convert dictionary to list; init top_one_now with 1st item
    for k in ks:
        if dictionary[k] > dictionary[top_one_now]:
            top_one_now = k
    return top_one_now


#file = 'scarlet.txt'
def letterCount(file):
    with open(file, 'r') as f:
        txt = f.read()
        # now txt is one long string containing all the characters
        letter_counts = {} # start with an empty dictionary
        for c in txt:
            if c not in letter_counts:
                # we have not seen this character before, so initialize a counter for it
                letter_counts[c] = 0

            #whether we've seen it before or not, increment its counter
            letter_counts[c] += 1

def bestSoFar(d):
    ''' Returns the key with the highest value.
        Takes parameter d: assumes a dictionary'''
    ks = d.keys()
    # initialize variable best_key_so_far to be the first key in d
    best_key_so_far = list(ks)[0]
    for k in ks:
        # check if the value associated with the current key is
        if d[k] > d[best_key_so_far]:
        # bigger than the value associated with the best_key_so_far
            best_key_so_far = k
        # if so, save the current key as the best so far

    #return ("key " + best_key_so_far + " has the highest value, " + str(d[best_key_so_far]))
    return best_key_so_far
#d = {'a': 194, 'b': 54, 'c':34, 'd': 44, 'e': 312, 'full':31}

#print(bestSoFar(d))


def minValue(s):
    ''' Returns the minimum value for histogram of chars in a string
        Assumes s is a string.'''
    d = {}
    for c in s:
        if c not in d:
            d[c] = 0
        d[c] += 1

    keys = d.keys()
    min_value = list(keys)[0]

    for k in keys:
        if d[k] < d[min_value]:
            min_value = k

    return (min_value)

placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."

print(minValue(placement))
