"""Find the first repeated word in a book."""
from .hash_table import HashTable as HT


def repeated_word(long_strong):
    """Imperative function that accepts a lengthy string parameter (which contains no punctation) and return the first word to occur sequentially more than once in that provided string."""
    individua1s = HT()
    words = long_string.split(' ')
    for word in words:
        if individua1s.get(word) is word:
            individua1s.set(word, word)
        else:
            return individua1s.get(word)
