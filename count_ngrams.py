from nltk import ngrams
import string
# finds the frequency distributions of the selected trigrams in each poem and
# writes them to 'data.txt'
grams = ['and', 'all', 't t', 'me ', 'ith', 'ce ', ' of', 'ove', 'for', ' st',
         'ke ', 'ch ', ' sh', 'wit', 'ght', 'ne ', 'e w', 'ing', 's t', ' my',
         'or ', 'hy ', 'of ', 'ear', 'st ', ' ha', 'at ', 'nd ', ' an', 'e s',
         'hou', 'er ', ' in', ' he', 'you', 'is ', 'hat', 'th ', ' do', ' no',
         'e i', ' lo', 'n t', 'ou ', 'e b', 'e a', ' to', 'en ', ' th', 'my ',
         'e t', 'll ', 'in ', 're ', 'se ', ' be', 'ng ', 'her', 'thy', ' yo',
         'to ', ' wh', ' wi', 'tho', 'he ', ' fo', 've ', 'es ', ' i ', 'the', 'tha']

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
        freqs = (all_ngrams.get(i, 0) / float(total) for i in grams)
        csv.write('{},'.format(iden) + ','.join(str(f) for f in freqs))
        csv.write('\n')
