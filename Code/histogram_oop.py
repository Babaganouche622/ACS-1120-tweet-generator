import string
import sys
import os
import random
import itertools

class Histogram:
    def __init__(self, source_text):
        self.total_words = set()
        self.hist = self._generate_histogram(source_text)

    def _generate_histogram(self, source_text):
        # Read the source text file or use the contents directly if provided as a string
        if isinstance(source_text, str):
            if os.path.isfile(source_text):
                try:
                    with open(source_text, 'r') as file:
                        text = file.read()
                except FileNotFoundError:
                    print(f"Error: File '{source_text}' not found.")
                    sys.exit(1)
            else:
                text = source_text
        elif isinstance(source_text, list):
            # Join the list elements into a single string
            text = " ".join(source_text)
        else:
            # Invalid input type, raise an exception or handle it accordingly
            raise ValueError("Invalid source_text type. Expected string or list.")


        # Remove punctuation and convert text to lowercase
        text = text.translate(str.maketrans('', '', string.punctuation)).lower()

        # Split the text into words
        words = text.split()
        self.total_words.update(words)

        # Create a dictionary to store word frequencies
        histogram = {}
        for word in words:
            histogram[word] = histogram.get(word, 0) + 1

        return histogram

    def unique_words(self):
        # Count the number of unique words in the histogram
        return len(self.hist)

    def frequency(self, word):
        # Get the frequency of the given word from the histogram
        return self.hist.get(word, 0)

    def generate_random_word(self):
        # Set the keys and weights
        keys = list(self.hist.keys())
        weights = list(self.hist.values())

        # Grab a random key based on the frequency of occurrence
        word = random.choices(keys, weights=weights)[0]

        return word

    def get_total_unique_words(self):
        # Count the unique words from the histogram
        return self.unique_words()

    def get_total_words(self):
        # Return the total number of words
        return len(self.total_words)

    def get_frequency(self, word):
        # Return the frequency of a given word
        return self.frequency(word)

    def get_random_word(self):
        # Return a random word based on a weighted system
        return self.generate_random_word()
    
    def get_word_frequencies(self):
        # Generate a list of tuples containing unique words and their frequencies
        return list(self.hist.items())

    def generate_random_phrase(self):

        random_words = []
        for _ in range(random.randint(1, 20)):
            random_words.append(self.generate_random_word().strip())
        phrase = " ".join(random_words)
        phrase = phrase.capitalize() + "."
        return phrase

    def get_random_phrase(self):
        return self.generate_random_phrase()


# def collect_data(source_text, num_runs, word):
#     # Create an instance of the Histogram class
#     histogram = Histogram(source_text)

#     unique_count = 0
#     mystery_count = 0
#     random_words = []

#     for _ in range(num_runs):
#         # Call the methods to get the desired values
#         unique_count += histogram.get_total_unique_words()
#         mystery_count += histogram.get_frequency(word)
#         random_words.append(histogram.get_random_word())

#     random_word_histogram = sorted(Histogram(random_words).get_word_frequencies(), key=lambda x: x[1], reverse=True)
#     return unique_count, histogram.get_total_words(), mystery_count, random_word_histogram


# Setup
fish_file = "./data/fish.txt"
dracula_file = "./data/dracula.txt"
# num_runs = int(sys.argv[2])
# sys_argv_file = f"./data/{sys.argv[1]}.txt"

# Call the collect_data method to collect the desired information
# unique_count, total_words, mystery_count, random_word_histogram = collect_data(sys_argv_file, num_runs, sys.argv[1])

# Print the final results
# print(f"""
# This is the setup:
# Total unique words: {unique_count}
# Total words: {total_words}
# Frequency of '{sys.argv[1]}': {mystery_count}
# Data Collection method was run {sys.argv[2]} times
# """)

# Print the list of word frequencies
# print("List of random words and frequency they were selected in the data collection:")
# for word, frequency in itertools.islice(random_word_histogram, 10):
#     print(f"{word}: {frequency}")
if __name__ == "__main__":
    hist = Histogram(dracula_file)
    for _ in range(random.randint(1, 5)):
        print(hist.get_random_phrase())
