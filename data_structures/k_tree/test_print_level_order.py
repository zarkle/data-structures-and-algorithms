from .k_tree import KTree as KT
from .print_level_order import print_level_order


def test_print_level_order(tree):
    """Test print_level_order."""
    assert print_level_order(tree) == '1 \n2 3 4 5 '


def test_print_level_order_small(small_tree):
    """Test print_level_order with small tree."""
    assert print_level_order(small_tree) == '1 \n2 3 '


def test_print_level_order_large(large_tree):
    """Test print_level_order with large tree."""
    assert print_level_order(large_tree) == '10 \n2 9 \n3 12 13 '
