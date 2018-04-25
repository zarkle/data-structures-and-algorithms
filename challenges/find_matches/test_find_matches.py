from .find_matches import find_matches as FM
import pytest


def test_find_match_no_tree():
    with pytest.raises(ValueError) as err:
        find_matches(tree, 5)
        assert err == 'Must provide tree'
