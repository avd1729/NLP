from nltk.corpus import gutenberg
import nltk
from nltk.corpus import wordnet
from nltk.draw.dispersion import dispersion_plot


book_ids = gutenberg.fileids()

print(book_ids[:1])  # 1-a

print()

for book_id in book_ids:  # 1-b
    print(book_id)

print()

search_text = "calendar"  # 1-c
for book_id in gutenberg.fileids():
    book_text = gutenberg.raw(book_id)
    if search_text in book_text:
        print(f'Found {search_text} in book : {book_id}')

print()


def word_similarity(word1, word2):  # 1-d
    # Get the synsets for the given words
    synsets1 = wordnet.synsets(word1)
    synsets2 = wordnet.synsets(word2)

    # Find the maximum similarity score between all pairs of synsets
    max_sim = 0
    for synset1 in synsets1:
        for synset2 in synsets2:
            sim = synset1.wup_similarity(synset2)
            if sim is not None and sim > max_sim:
                max_sim = sim

    return max_sim


# Example usage
word1 = 'king'
word2 = 'queen'
similarity = word_similarity(word1, word2)
print(f'The similarity between {word1} and {word2} is {similarity:.2f}')

print()
