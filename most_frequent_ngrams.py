from nltk import ngrams
import string

# util file to figure out which ngrams to use as inputs
all_ngrams = set()
author_poems = {'shakespeare': 154, 'spenser': 89}
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
        if float(count) / total > 0.003:
            all_ngrams.add(ngram)
    print all_ngrams
