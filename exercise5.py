'''
Accessing text corpora and lexical resources:
	a)identify the fields that are available in austen emma,gutenberg electronic text.
	b)find out the no of words it contains.
	c)write a short program to display other information about each text and compute
  	the statistics for each text.
	d)identify a text,split into tokens and identify how many letters occur in the text.
'''

import nltk
from nltk.corpus import gutenberg


# Load the Gutenberg corpus and access the fields for Emma
emma = gutenberg.raw('austen-emma.txt')

# a
# Print the first 30 characters of the text to get a sense of its content
print(emma[:30])
print()

# b
print(len([i for i in emma]))
print()

# c
print("Information about the Emma text:")
print("Title: Emma")
print("Author: Jane Austen")
print("Number of characters in the text:", len(emma))
print("Number of words in the text:", len(nltk.word_tokenize(emma)))
print("Number of sentences in the text:", len(nltk.sent_tokenize(emma)))
print("\n")

# d
words = nltk.word_tokenize(emma[:100])
for i in words:
    for j in i:
        print(j, end=' ')
