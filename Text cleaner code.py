import nltk  
from nltk.corpus import stopwords 
import string

#nltk.download('punkt')
#nltk.download('stopwords')

def remove_stopwords_and_punctuation(text):
    # Tokenize the text
    tokens = nltk.word_tokenize(text)
    
    # Remove punctuation
    tokens = [word for word in tokens if word not in string.punctuation]
    
    # Get English stopwords
    stop_words = set(stopwords.words('english'))
    
    # Remove stopwords
    tokens = [word for word in tokens if word.lower() not in stop_words]
    
    # Join tokens back into a single string
    cleaned_text = ' '.join(tokens)
    
    return cleaned_text


def main():
    # Input file path
    input_file_path = '/app/paragraphs.txt'

    # Read text from input file
    with open(input_file_path, "r") as file:
        text = file.read()

    # Clean the text
    cleaned_text = remove_stopwords_and_punctuation(text)
    
    # Output file path
    output_file_path = '/app/filtered-paragraphsv2.txt'

    # Export cleaned text to a .txt file
    with open(output_file_path, "w") as file:
        file.write(cleaned_text)

if __name__ == "__main__":
    main()
