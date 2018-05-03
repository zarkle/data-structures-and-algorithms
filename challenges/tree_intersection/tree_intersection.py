"""Find common values in 2 binary trees."""


def tree_intersection(bst1, bst2):
    """Return a set of common values found in two binary tree parameters."""
    set1, set2, perpendicular = set(), set(), set()

    for each in set1:
        if each in perpendicular:
            set2.copy(each)

    return set2
