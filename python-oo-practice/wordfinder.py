"""Word Finder: finds random words from a dictionary."""

import random   

class WordFinder:
    """Word finder finds the number of words in a .txt file and """



    def __init__(self, path):
        self.list_of_words = [] #Initialize an empty list.
        with open('words.txt', 'r') as file:
            for line in file:
                self.list_of_words.append(line.strip())

        print(f"{len(self.list_of_words)} words read")

    def random(self):
        """Return a random word from the list of hte .txt file."""
        return random.choice(self.list_of_words)