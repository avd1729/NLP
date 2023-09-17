'''
1.Access Text corpora and lexical resources:	
	a) use spell checks to find unusual or misspelt words in a text corpus.
	b)Filter the stop words present in a document
	c)Compute what fraction of words in a text is not in the stop words list.
	d)Find out the words whose pronunciation ends with a syllable sounding like a word which you choose.
	e)Use word n35 qne rine ou5 5h3 wynonymouw 2o4ew or q tif3n 2o4e.
	f)Implement hyponyms and hypernyms for a particular word in the given text.
	g)Accessing text from the web-extract data from web and provide insights about it.
'''
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.corpus import cmudict
from nltk.corpus import stopwords
import nltk
from nltk.corpus import words

# Load a reference list of English words from NLTK
english_words = set(words.words())

# Sample text corpus (you can replace this with your own corpus)
text_corpus = "Thsi is an exmaple sentnce with sum mispleld worsd."

# Tokenize the text into words
words_in_corpus = nltk.word_tokenize(text_corpus)

# Find unusual or misspelled words
misspelled_words = set()
for word in words_in_corpus:
    if word.lower() not in english_words:
        misspelled_words.add(word.lower())

# Print the misspelled words
print("Misspelled or Unusual Words:")
print(misspelled_words)
print()

# Sample document (replace with your own text)
document = "This is a sample document containing some stop words such as 'the', 'and', 'is', etc."

# Tokenize the document into words
words = nltk.word_tokenize(document)

# Create a set of stopwords from NLTK's corpus
stop_words = set(stopwords.words("english"))

# Filter out the stopwords
filtered_words = [word for word in words if word.lower() not in stop_words]

# Reconstruct the filtered document
filtered_document = " ".join(filtered_words)

# Print the filtered document
print("Original Document:")
print(document)
print("\nFiltered Document:")
print(filtered_document)
print()

# Count the number of words in the text that are not in the stopwords list
non_stopword_count = sum(1 for word in words if word.lower() not in stop_words)

# Compute the fraction
total_word_count = len(words)
fraction_non_stopwords = non_stopword_count / total_word_count

# Print the results
print("Total Words:", total_word_count)
print("Non-Stop Words Count:", non_stopword_count)
print("Fraction of Non-Stop Words:", fraction_non_stopwords)
print()


# Load the CMU Pronouncing Dictionary
pronouncing_dict = nltk.corpus.cmudict.dict()

# Define the target word for the ending syllable
target_word = "melon"  # Replace with your chosen word

# Function to check if a word's pronunciation ends with the target syllable


def ends_with_target_syllable(word):
    if word in pronouncing_dict:
        pronunciations = pronouncing_dict[word]
        for pronunciation in pronunciations:
            # Check if the last syllable's pronunciation matches the target word's pronunciation
            last_syllable_pronunciation = "".join(pronunciation[-1])
            if last_syllable_pronunciation == target_word:
                return True
    return False


# List of words to check (you can replace this with your own word list)
word_list = ["banana", "orange", "apple", "pineapple", "watermelon"]

# Find and print words that match the criteria
matching_words = [
    word for word in word_list if ends_with_target_syllable(word)]
print("Words whose pronunciation ends with a syllable sounding like '{}':".format(target_word))
for word in matching_words:
    print(word)
print()


# Define the word for which you want to find synonyms
word = "happy"

# Initialize a list to store synonyms
synonyms = []

# Find synsets for the word
synsets = wordnet.synsets(word)

# Extract synonyms from the synsets
for synset in synsets:
    for lemma in synset.lemmas():
        synonyms.append(lemma.name())

# Remove duplicates and print the synonyms
synonyms = list(set(synonyms))
print(f"Synonyms for '{word}':")
print(synonyms)
print()


# Sample text (replace with your own text)
text = "The dog chased the cat. The cat climbed a tree."

# Tokenize the text into words
words = word_tokenize(text)

# Define the target word for which you want to find hyponyms and hypernyms
target_word = "cat"  # Replace with the word you're interested in

# Initialize lists to store hyponyms and hypernyms
hyponyms = []
hypernyms = []

# Find synsets for the target word
synsets = wordnet.synsets(target_word)

# Loop through each synset to find hyponyms and hypernyms
for synset in synsets:
    hyponyms.extend(synset.hyponyms())
    hypernyms.extend(synset.hypernyms())

# Extract lemma names (words) from hyponyms and hypernyms
hyponym_words = [lemma.name()
                 for synset in hyponyms for lemma in synset.lemmas()]
hypernym_words = [lemma.name()
                  for synset in hypernyms for lemma in synset.lemmas()]

# Remove duplicates from the lists
hyponym_words = list(set(hyponym_words))
hypernym_words = list(set(hypernym_words))

# Print the hyponyms and hypernyms
print(f"Hyponyms of '{target_word}':")
print(hyponym_words)

print(f"\nHypernyms of '{target_word}':")
print(hypernym_words)
print()
