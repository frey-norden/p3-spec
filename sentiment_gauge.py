def strip_punctuation(s):
    ''' takes a string s and strips the puncs
        returns a new string of only letters '''

    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

    new_string = ''

    for letter in s:
        if letter not in punctuation_chars:
            new_string += letter

    return new_string

def clean_wrds(s):
    ''' takes string s, converts to lower case
        returns a list of words '''

    clean_wrds = []  # initialize list
    # clean up incoming string given as parameter
    wrds = s.lower().split()
    for w in wrds:
        clean_wrds.append(strip_punctuation(w))

    return clean_wrds

def get_pos(s):
    ''' takes string s, cleans it, tests and
        returns count of positive words '''

    wrds = clean_wrds(s)  # initialize list
    # clean up incoming string given as parameter

    count = 0
    # list of positive words to use
    positive_words = []
    with open("positive_words.txt") as pos_f:
        for lin in pos_f:
            if lin[0] != ';' and lin[0] != '\n':
                positive_words.append(lin.strip())

    for w in wrds:
        if w in positive_words:
            count += 1

    return count

def get_neg(s):
    ''' takes string s, cleans it, tests and
        returns count of positive words '''

    wrds = clean_wrds(s)

    count = 0
    # list of negatiivi words to use
    negative_words = []
    with open("negative_words.txt") as pos_f:
        for lin in pos_f:
            if lin[0] != ';' and lin[0] != '\n':
                negative_words.append(lin.strip())

    for w in wrds:
        if w in negative_words:
            count += 1

    return count

def get_twitter_data(twitter_data):
    ''' takes a csv input file, reads, processes and outputs to results csv file
        void function - does not return a value '''
    # writeout headings on first line
    res.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n')
    # open and test the databanks && writeout resultant data to file

    lines = td.readlines()
    scrapJunk = lines.pop(0)
    for line in lines:
        dataList = line.strip().split(',')
        res.write('{}, {}, {}, {}, {}'.format(dataList[1], dataList[2], get_pos(dataList[0]), get_neg(dataList[0]), (get_pos(dataList[0]) - get_neg(dataList[0]))))
        res.write('\n')

input_file = 'project_twitter_data.csv'
td = open(input_file, 'r')

results = 'resulting_data.csv'
res = open(results, 'w')

get_twitter_data(td)

td.close()
res.close()
