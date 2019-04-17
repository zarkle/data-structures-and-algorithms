from .BST_nearest_val import nearest_val as NV


def test_BST_nearest_val_example_one():
    data = sorted([1, 3, 6, 4, 7, 8, 10, 14, 13])
    assert NV(data, 9) == 10


def test_BST_nearest_val_example_two():
    data = sorted([8, 3, 1, 6, 4, 7, 10, 14, 13])
    assert NV(data, 13) == 13


def test_BST_nearest_val_example_three():
    data = sorted([8, 3, 1, 6, 4, 7, 10, 14, 13])
    assert NV(data, 0) == 1


def test_BST_nearest_val_final_one():
    data = sorted([15, 20, 7, 9, 3, 32, 17])
    assert NV(data, 13) == 15


def test_BST_nearest_val_final_two():
    data = sorted([15, 20, 7, 9, 3, 32, 17])
    assert NV(data, 30) == 32


def test_BST_nearest_val_duplicates():
    data = sorted([15, 20, 7, 9, 20, 32, 32])
    assert NV(data, 30) == 32
