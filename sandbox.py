#!/usr/bin/env python
"""
A sandbox for trying out ideas whilst learning Python
"""

import collections as C
import csv
import math
import traceback

def is_anagram(word1, word2):
    return C.Counter(word1) == C.Counter(word2)

def binary_powers(count):
    """Returns a list of binary powers, with the count specified by an argument"""
    return map(lambda x: 2 ** x, range(count))

def intersect(*args):
    res = []
    for x in args[0]:
        if x in res: continue
        for other in args[1:]:
            if x not in other: break
        else:
            res.append(x)
    return res

def union(*args):
    res = []
    for seq in args:
        for x in seq:
            if not x in res:
                res.append(x)
    return res

##########################################################################

n = 0
ok = True
while not ok:
    try:
        n = int(raw_input('Enter an integral number of at least 2: '))
        if n < 2:
            print('Please choose a value of at least 2')
            continue
        ok = True
    except Exception as X:
        print('Oops [{0}]; try again'.format(X))
        continue

##########################################################################

# CSV
verbose = True
print('\nReading CSV file...')
filename = 'small.csv'
headers = ['First', 'Last', 'Contact']
linecount = 0
try:
    f = open(filename)
    f_csv = csv.DictReader(f, headers)
    header_row = next(f_csv)
    for row in f_csv:
        linecount += 1
        if verbose: print('Email: {0}'.format(row['Contact']))
except Exception as X:
    print('Ooops ... something went wrong: ', X)
    traceback.print_exc()
finally:
    print ('Closing the file')
    f.close()

print('Read {0} lines'.format(linecount))

##########################################################################

if __name__ == '__main__':
    print ('\nSELF-TESTING\n')

    print('Binary powers:', binary_powers(10))

    print ('Intersections and Unions')
    s1, s2, s3 = 'SPAM', 'SCAM', 'SCOT'
    print(s1, s2, s3)
    print('Intersection: {0}; Union: {1}', intersect(s1, s2, s3), union(s1,s2,s3))
