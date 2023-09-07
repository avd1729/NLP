import random
from nltk.corpus import brown


# Select a category (e.g., "news")
category = "news"

# Get the words from the selected category
words = brown.words(categories=category)

# Generate a few random sentences using these words
num_sentences = 3

for _ in range(num_sentences):
    # Select a random starting point in the list of words
    # Prevent index out of range
    start_index = random.randint(0, len(words) - 10)

    # Generate a sentence of random length (between 5 and 15 words)
    sentence_length = random.randint(5, 15)
    end_index = start_index + sentence_length

    # Ensure the end index does not go beyond the word list
    if end_index >= len(words):
        end_index = len(words) - 1

    # Extract the words for the sentence
    sentence_words = words[start_index:end_index]

    # Join the words to form a sentence
    sentence = ' '.join(sentence_words)

    # Capitalize the first letter and add a period at the end
    sentence = sentence.capitalize() + '.'

    # Print the generated sentence
    print(sentence)
