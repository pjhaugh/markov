# Patrick Haugh
# Dec 2017
# MIT License

from corpus import Corpus
from collections import Counter
from random import choices


class Markov:
    """
    Psuedorandom stateful text generator based on input corpus
    """

    def __init__(self, text=None, path=None):
        self.corpus = Corpus(text, path)
        self.state, *_ = choices(
            *zip(*(sum(self.corpus.values(), Counter()).items())))
        if self.state == '.':
            _ = next(self)

    def __iter__(self):
        return self

    def __next__(self):
        curr_state = self.state
        self.state, *_ = choices(*zip(*self.corpus[self.state].items()))
        return curr_state
