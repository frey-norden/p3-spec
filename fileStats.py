#-*- utf-8 -*-

''' Function assumes a string for filename as input.
    Returns the number of chars in the file'''

def numCharFile(file):

    num_chars = 0
    with open(file, 'r') as f:
        for line in f:
            num_chars += len(line)

    return num_chars



def numLinesFile(file):
    num_lines = 0
    with open(file, 'r') as f:
        lines = f.readlines()
        num_lines += len(lines)

    return num_lines

def readChars(file, n):
    num_chars = ''
    with open(file, 'r') as f:
        text = f.read()
        num_chars += text[:int(n)]

    return num_chars

filename = input('Enter the txt file name: ')
n = input('Hur monga bokstaver till lesa: ')
print('Number of chars:', numCharFile(filename))
print('Number of lines:', numLinesFile(filename))
print('First {} chars of file: {}'.format(n, readChars(filename, n)))
