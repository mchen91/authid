from nltk import ngrams
import string

all_ngrams = {}
num_poems = 89
author = 'spense'

for i in xrange(1, num_poems + 1):
    with open('{}{}'.format(author, i), 'r') as f:
        text = ' '.join(line.strip().lower() for line in f)
        text = ''.join(c for c in text if c not in string.punctuation)
        trigrams = [''.join(i) for i in ngrams(text, 3)]
        print trigrams

        for t in trigrams:
            all_ngrams[t] = all_ngrams.get(t, 0) + 1

total = sum(all_ngrams.values())
different = len([i for i in all_ngrams.values() if i > 1])
print "total trigrams: {}".format(total)
for i in sorted(all_ngrams.items(), key=lambda x:x[1], reverse=True)[:10]:
    print i[0], i[1], '{0:.2f}%'.format(float(i[1]) / total * 100)
#import pdb;pdb.set_trace()
