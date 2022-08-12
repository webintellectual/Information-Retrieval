#!/opt/homebrew/bin/python3

import sys
import string,re

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip().lower()
    #line = ''.join(ch for ch in line if ch not in string.punctuation)
    #line.replace("_"," ")
    line = re.sub(r'[^a-z0-9]',' ',line) #regular expression to remove the punctuations

    words = line.split() # split the line into words

    # increase counters
    for i in range(len(words)):
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        # tab-delimited; the trivial word count is 1
        try:
            word = words[i]+","+words[i+1]
        except:
            word = words[i]+", "
        print ('%s\t%s' % (word, 1))