import random
import sys

random_number = int(sys.argv[1])

def generate_random_word():
    with open("/usr/share/dict/words", "r") as f:
        words = f.readlines()
    
    random_word = []
    for _ in range(random_number):
      random_word.append(random.choice(words).strip())
    return " ".join(random_word)

# Usage example
random_word = generate_random_word()
random_word = random_word.capitalize() + "."

if __name__ == '__main__':
  quote = random_word
  print("Random word:", random_word)