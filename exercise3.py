from collections import Counter
import nltk
from nltk.corpus import brown
from nltk.tokenize import word_tokenize
from nltk.util import bigrams
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures

# 3 - a

brown_words = brown.words()
long_words = [word for word in brown_words if len(word) > 10]
print("The First five words that are more than 10 characters long are : ")
print(long_words[:5])

print()


# 3 - c
count = Counter(long_words)

print(count.most_common(5))
print()

# 3 - d

text = "This is an example sentence for finding bigrams and collocations using NLTK in Python."
tokens = word_tokenize(text)

bigram_list = list(bigrams(tokens))
print("Bigrams:")
for bigram in bigram_list:
    print(bigram)

finder = BigramCollocationFinder.from_words(tokens)
# You can adjust the number of collocations to retrieve
collocations = finder.nbest(BigramAssocMeasures.pmi, 10)

print("\nCollocations:")
for collocation in collocations:
    print(" ".join(collocation))

print()

# 3 - e

print(count.most_common(1))
