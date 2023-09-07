import nltk
from nltk.corpus import treebank

words = treebank.words()

starts_with_s = 0
ends_with_s = 0
z_in_word = 0
word_is_lower = 0
word_is_upper = 0
word_is_alpha = 0
word_is_alnum = 0
word_is_digit = 0
word_is_title = 0

for word in words:
    if word.startswith('s'):
        starts_with_s += 1
    if word.endswith('s'):
        ends_with_s += 1
    if 'z' in word:
        z_in_word += 1
    if word.islower():
        word_is_lower += 1
    if word.isupper():
        word_is_upper += 1
    if word.isalpha():
        word_is_alpha += 1
    if word.isalnum():
        word_is_alnum += 1
    if word.isdigit():
        word_is_digit += 1
    if word.istitle():
        word_is_title += 1

print(starts_with_s)
print(ends_with_s)
print(z_in_word)
print(word_is_lower)
print(word_is_upper)
print(word_is_alpha)
print(word_is_alnum)
print(word_is_digit)
print(word_is_title)
