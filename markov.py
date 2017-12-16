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
            next(self)

    def __iter__(self):
        return self

    def __next__(self):
        curr_state = self.state
        self.state, *_ = choices(*zip(*self.corpus[self.state].items()))
        return curr_state

    def get_sentences(self, n=1):
        return ' '.join(Markov._merge_periods(self._yield_sentences(n)))

    def _yield_sentences(self, n):
        while n:
            state = next(self)
            if state == '.':
                n -= 1
            yield state

    @staticmethod
    def _merge_periods(iterable):
        out = []
        for word in iterable:
            if word == '.' and out:
                out[-1] += '.'
            else:
                out.append(word)
        return out
