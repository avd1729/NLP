from nltk.corpus import brown
import nltk

# Get a list of genre categories in the Brown Corpus
genres = brown.categories()

# Calculate and print lexical diversity for each genre
for genre in genres:
    words = brown.words(categories=genre)
    unique_words = set(words)
    lexical_diversity = len(unique_words) / len(words)
    print(f"Genre: {genre}, Lexical Diversity: {lexical_diversity:.2f}")
