"""Word Finder: finds random words from a dictionary."""

from random import choice
from readline import read_init_file


class WordFinder:
    """ Finds random words in a 1-word-per-line dictionary file """    

    def __init__(self, file_path):
        self.file_path = file_path
        self.words = self.read_file(file_path)
        print(f"There are {len(self.words)} word(s) read");

    def read_file(self, file_path):
        """ Creates a list of all words in the dictionary """

        self.input_file = open(file_path, "r")
        words = [word for word in self.input_file]
        self.input_file.close()

        return words
    
    def random(self):
        """ Randomized search of 1 word """

        return choice(self.words).strip()


class SpecialWordFinder(WordFinder):
    """ Finds words withou # and removes blank lines"""

    def read_file(self, file_path):
        self.input_file = open(file_path, "r")
        words = [ word for word in self.input_file if not word.startswith("#") and word.strip()]
        self.input_file.close()
        
        return words




