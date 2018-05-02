"""Find common values in 2 binary trees."""


def tree_intersection(bst1, bst2):
    """Return a set of common values found in two binary tree parameters."""
    set1, set2, perpendicular = set(), set(), set()

    bst1.pre_order(lambda n: set1.add(n.val))
    bst2.pre_order(lambda n: set2.add(n.val))

    for each in set1:
        if each in set2:
            perpendicular.add(each)

    return perpendicular
