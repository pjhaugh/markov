# Patrick Haugh
# Dec 2017
# MIT License

from collections import defaultdict, Counter
from itertools import islice
from re import sub


def sliding_window(iterable):
    """
    Takes an iterable i0, i1, i2, i3...
    Returns a generator (i0, i1), (i1, i2), (i2, i3) 
    """
    return zip(iterable, islice(iterable, 1, None))


class Corpus(defaultdict):
    """
    Process a body of text to find the weights for next words. Takes a string
    and a file pointer.
    """

    def __init__(self, text=None, path=None):
        super().__init__(Counter)
        if text:
            self.update(text)
        if path:
            with open(path) as file:
                self.update(file.read())

    def update(self, text):
        """
        Processes the text input and adds it to the Corpus
        """
        split_text = Corpus.split_text(text)
        pairs = sliding_window(split_text)
        for pred, succ in pairs:
            self[pred][succ] += 1

    @staticmethod
    def split_text(text):
        """
        Moves the periods off the ends of sentences so that The end of the
        sentence is treated as its own "word"
        """
        return sub(r'(?<=\w)\.', ' .', text).split()
