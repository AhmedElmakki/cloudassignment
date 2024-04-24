from collections import Counter
from nltk.corpus import stopwords
import os


file_path = '/app/filtered-paragraphsv2.txt'  # Path to the file inside the Docker container

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        # Process the file (e.g., read its contents)
        content = file.read()
        #print(content)
except FileNotFoundError:
    print(f"File '{file_path}' not found.")

def count_words_in_file(file_path):
    # Initialize a Counter to store word counts
    word_counts = Counter()

    # Open the text file for reading
    with open(file_path, 'r', encoding='utf-8') as file:
        # Read the file line by line
        for line in file:
            # Tokenize the line into words (split by whitespace)
            words = line.strip().split()
            
            # Normalize words (convert to lowercase, remove punctuation, etc.)
            normalized_words = [word.lower() for word in words]
            
            # Update the word counts using Counter
            word_counts.update(normalized_words)

    return word_counts

word_counts = count_words_in_file(file_path)


print("Word Frequencies:")
for word, count in word_counts.most_common():
    print(f"{word}: {count}")

