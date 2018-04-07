"""Recursion solution from Adam"""
MAP = dict(zip('[({', '])}'))


def recursion(it, opener=None):
    for c in it:
        if c in MAP.keys():
            if not recursion(it, c):
                return False
        if opener is not None and MAP[opener] == c:
            return True
        if c in MAP.values():
            return False
    return True if opener is None else False


def multi_bracket_validation(input):
    """
    Test input string for matching brackets.

    Valid input look as follows:
    - `[[[[]]]]`
    - `[][]{}`
    - `{()}({})`

    Invalid inputs could be as follows:
    - `(()}`
    - `}}`
    - `][`
    """
    return recursion(iter(input))
