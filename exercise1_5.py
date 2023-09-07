import nltk

# Example text
text = "This is an example text. It contains several words, some of which are repeated."

# Tokenize the text into words
words = nltk.word_tokenize(text)

# Create a vocabulary set
vocab = set(words)

# Print the vocabulary items
print(sorted(vocab))
