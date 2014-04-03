from nltk import ngrams
import string

# string operators
punctuationCount = lambda l1, l2: len(list(filter(lambda c: c in l2, l1)))

# util file to figure out which ngrams to use as inputs
common_ngrams = set()
author_poems = {'shakespeare': 154, 'spenser': 89, 'philip': 100}
for auth, num_poems in author_poems.iteritems():
    auth_ngrams = {}
    # duplicate input data
    for i in xrange(1, max(author_poems.values()) + 1):
        with open('{}/{}{}'.format(auth, auth, i % num_poems + 1 if i > num_poems else i), 'r') as f:
            text = ' '.join(line.strip().lower() for line in f)
            text = text.translate(string.maketrans('', ''), string.punctuation)
            # wordList = text.split()
            # wordLengths=[len(word) for word in wordList] 
            # averageWordLength = sum(wordLengths)/float(len(wordList))
            # print averageWordLength
            trigrams = [''.join(i) for i in ngrams(text, 3)]

            for t in trigrams:
                auth_ngrams[t] = auth_ngrams.get(t, 0) + 1
    total = sum(auth_ngrams.values())
    # for each author, grab the ngrams that appear more than 0.3% of the time
    for ngram, count in auth_ngrams.items():
        if float(count) / total > 0.0025: # if float(count) / total > 0.0025:
            common_ngrams.add(ngram)

# second pass over files to create input data
csv = open('data.txt', 'w')
for iden, (auth, num_poems) in enumerate(author_poems.items(), start=1):
    for i in xrange(1, max(author_poems.values()) + 1):
        all_ngrams = {}
        with open('{}/{}{}'.format(auth, auth, i % num_poems + 1 if i > num_poems else i)) as f:
            text = ' '.join(line.strip().lower() for line in f)
        puncCount = punctuationCount(text,string.punctuation)/float(text.count('.') + text.count('!') + text.count('?'))
        commaPerSentence = float(text.count(',')) / (text.count('.') + text.count('!') + text.count('?'))
        text = text.translate(string.maketrans('', ''), string.punctuation)
        trigrams = [''.join(i) for i in ngrams(text, 3)]

        for t in trigrams:
            all_ngrams[t] = all_ngrams.get(t, 0) + 1

        total = sum(all_ngrams.values())
        freqs = (all_ngrams.get(i, 0) / float(total) for i in common_ngrams)
        csv.write('{},'.format(iden) + ','.join(str(f) for f in freqs))
        csv.write(', %f' % puncCount)
        csv.write(', %f' % commaPerSentence)
        csv.write('\n')
csv.close()
