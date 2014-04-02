from nltk import ngrams
import string
# finds the frequency distributions of the selected trigrams in each poem and
# writes them to 'data.txt'
grams = ['and', 't t', 'me ', ' of', ' th', ' sh', 'my ', 'ing', 's t',
         ' my', 'or ', 'hy ', 'of ', 'st ', 'at ', 're ', ' an', 'hou',
         'er ', ' in', 'you', 'is ', 'hat', 'th ', ' be', ' no', ' lo',
         'n t', 'ou ', 'e a', ' to', 'se ', 'e w', 'e t', 'll ', 'in ',
         'to ', 'en ', 'es ', 'ng ', 'for', 'thy', ' yo', ' wh', ' wi',
         'tho', 'he ', ' fo', 've ', 'nd ', ' i ', 'the', 'tha']

csv = open('data.txt', 'w')
authors = ['shakespeare', 'spenser']
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
        freqs = (all_ngrams.get(i, 0) / float(total) for i in grams)
        csv.write('{},'.format(iden) + ','.join(str(f) for f in freqs))
        csv.write('\n')
