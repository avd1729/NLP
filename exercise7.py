'''
2.Regular expressions for detecting word patterns (word corpus)
	a)Find words ending with 'ed' using endswith.
	b)Check whether the patter 'p'can be found inside the strings 's'.
	c)Extracting letters from a word(vowels or consonants) and find the relative frequency of them.
	d)Find word stems.
	e) Normalize the text(eg:The,the)-Tokenize and lemmatization
	f)Text Wrapping
'''

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
import nltk
import re

# Sample word corpus (replace with your actual corpus)
corpus = "I walked to the park, and she danced in the rain. They talked about the book they read."

# Use regular expression to find words ending with 'ed'
words_ending_with_ed = re.findall(r'\b\w+ed\b', corpus)

# Print the words found
print("Words ending with 'ed':")
for word in words_ending_with_ed:
    print(word)

print()

# Define the strings
s1 = "This is a sample string."
s2 = "Another string with a pattern."

# Define the pattern to search for
p = "p"

# Check if 'p' is in each string
if p in s1:
    print(f"'{p}' is found in '{s1}'")
else:
    print(f"'{p}' is not found in '{s1}'")

if p in s2:
    print(f"'{p}' is found in '{s2}'")
else:
    print(f"'{p}' is not found in '{s2}'")

# Define the word from which you want to extract letters
word = "example"

# Define whether you want to extract vowels or consonants
# Set to "vowels" or "consonants"
choice = "vowels"

# Initialize counters for vowels and consonants
vowel_count = 0
consonant_count = 0

# Convert the word to lowercase for case-insensitive matching
word = word.lower()

# Define the sets of vowels and consonants
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"

# Iterate through each letter in the word and count the occurrences
for letter in word:
    if choice == "vowels" and letter in vowels:
        vowel_count += 1
    elif choice == "consonants" and letter in consonants:
        consonant_count += 1

# Calculate the total number of letters in the word
total_letters = len(word)

# Calculate the relative frequencies
if choice == "vowels":
    relative_frequency = vowel_count / total_letters
    print(
        f"Vowels: {vowel_count} ({relative_frequency:.2%} relative frequency)")
elif choice == "consonants":
    relative_frequency = consonant_count / total_letters
    print(
        f"Consonants: {consonant_count} ({relative_frequency:.2%} relative frequency)")
else:
    print("Invalid choice. Please choose 'vowels' or 'consonants'.")

print()


# Sample text (replace with your own text)
text = "The quick brown foxes jumped over the lazy dogs. Jumping and jumped are forms of jump."

# Tokenize the text into words
words = nltk.word_tokenize(text)

# Initialize the Porter stemmer
stemmer = PorterStemmer()

# Find word stems for each word in the text
stems = [stemmer.stem(word) for word in words]

# Print the original words and their corresponding stems
for word, stem in zip(words, stems):
    print(f"{word} => {stem}")

print()
# Normalize the text by converting words to lowercase
words = [word.lower() for word in words]

# Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word not in stop_words]

# Initialize the WordNet lemmatizer
lemmatizer = WordNetLemmatizer()

# Lemmatize the words
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]

# Print the normalized and lemmatized words
print("Original Words:")
print(words)
print("\nNormalized and Lemmatized Words:")
print(lemmatized_words)
