import nltk
import random
from nltk.corpus import brown

# Train a bigram model on the Brown corpus
bigrams = nltk.bigrams(brown.words())
cfd = nltk.ConditionalFreqDist(bigrams)

# Generate random text
word = 'the'
num_words = 10
for i in range(num_words):
    print(word, end=' ')
    if word in cfd:
        word = random.choice(list(cfd[word].keys()))
    else:
        break
