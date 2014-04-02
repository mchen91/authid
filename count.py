from nltk import ngrams
import string

# util file to figure out which ngrams to use as inputs
common_ngrams = set()
author_poems = {'shakespeare': 154, 'spenser': 89, 'philip': 100}
for auth, num_poems in author_poems.iteritems():
    auth_ngrams = {}
    # spenser only has 89 poems
    for i in xrange(1, 90):#num_poems + 1):
        with open('{}/{}{}'.format(auth, auth, i), 'r') as f:
            text = ' '.join(line.strip().lower() for line in f)
            text = text.translate(string.maketrans('', ''), string.punctuation)
            trigrams = [''.join(i) for i in ngrams(text, 3)]

            for t in trigrams:
                auth_ngrams[t] = auth_ngrams.get(t, 0) + 1
    total = sum(auth_ngrams.values())
    # for each author, grab the ngrams that appear more than 0.3% of the time
    for ngram, count in auth_ngrams.items():
        if float(count) / total > 0.0025:
            common_ngrams.add(ngram)

# second pass over files to create input data
csv = open('data.txt', 'w')
authors = ['shakespeare', 'spenser', 'philip']
for iden, auth in enumerate(authors, start=1):
    for i in xrange(1, 90):
        all_ngrams = {}
        with open('{}/{}{}'.format(auth, auth, i)) as f:
            text = ' '.join(line.strip().lower() for line in f)
        text = text.translate(string.maketrans('', ''), string.punctuation)
        trigrams = [''.join(i) for i in ngrams(text, 3)]

        for t in trigrams:
            all_ngrams[t] = all_ngrams.get(t, 0) + 1

        total = sum(all_ngrams.values())
        freqs = (all_ngrams.get(i, 0) / float(total) for i in common_ngrams)
        csv.write('{},'.format(iden) + ','.join(str(f) for f in freqs))
        csv.write('\n')

