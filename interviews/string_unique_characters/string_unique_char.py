from .hash_table import HashTable as HT


def unique_char(string):
    """."""
    individuals = set()
    for char in string.lower():
        if char == ' ':
            pass
        if char in individuals:
            return False
        individuals.add(char)
    return True
