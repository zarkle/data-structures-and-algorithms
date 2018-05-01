"""Find the first repeated word in a book."""
from .hash_table import HashTable as HT


def repeated_word(long_string):
    """Imperative function that accepts a lengthy string parameter (which contains no punctation) and return the first word to occur sequentially more than once in that provided string."""
    if type(long_string) is not str:
        raise TypeError('Input must be string.')

    individuals = HT()
    words = long_string.lower().split(' ')
    for word in words:
        if individuals.get(word) is None:
            individuals.set(word, word)
        else:
            return word
