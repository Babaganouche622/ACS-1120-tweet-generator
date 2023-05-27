"""Main script, uses other modules to generate sentences."""
from flask import Flask
import random
from dictionary_words import generate_random_quote


app = Flask(__name__)

# TODO: Initialize your histogram, hash table, or markov chain here.
# Any code placed here will run only once, when the server starts.
def random_words():
    random_number = random.randint(1, 100)
    return generate_random_quote(random_number)

@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    return f"<p>{random_words()}</p>"


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
