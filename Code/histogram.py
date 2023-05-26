import string
import sys
import os

total_words = ""

def histogram(source_text):
    global total_words
    # Read the source text file or use the contents directly if provided as a string
    if isinstance(source_text, str) and os.path.isfile(source_text):
        with open(source_text, 'r') as file:
            text = file.read()
    else:
        text = source_text

    # Remove punctuation and convert text to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()

    # Split the text into words
    words = text.split()
    total_words = words
    # Create a dictionary to store word frequencies
    histogram = {}
    for word in words:
        histogram[word] = histogram.get(word, 0) + 1

    return histogram

def unique_words(histogram):
    # Count the number of unique words in the histogram
    return len(histogram)

def frequency(word, histogram):
    # Get the frequency of the given word from the histogram
    return histogram.get(word, 0)

# Example usage
source_text = """
In this tutorial, we\’ll be writing a program which, given a source body of text, can perform operations to answer questions such as:

What is the least/most frequent word(s)?
How many different words are used?
What is the average (mean/median/mode) frequency of words in the text?
The structure to represent this kind of data is called a histogram, which really just means a count of things by category. In Python, you can represent a histogram in a variety of ways using the different data structures available. Part of the challenge of this tutorial is how to design and use these data structures to create a histogram.
"""  # Replace with the path to your source text file or provide the contents as a string

dracula_file = "./data/dracula.txt"

hist = histogram(dracula_file)
# hist = histogram(source_text)
unique_count = unique_words(hist)
mystery_count = frequency(sys.argv[1], hist)

print("Total unique words:", unique_count)
print("Total words:", len(total_words))
print(f"Frequency of '{sys.argv[1]}':", mystery_count)
