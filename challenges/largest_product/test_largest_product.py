from largest_product import largest_product


def test_largest_product():
    assert largest_product([[1, 2], [3, 4], [5, 6], [7, 8]]) == 56


def test_largest_product_long():
    assert largest_product([[8, 20], [5, 4], [100, 100], [8, 2], [9, 3], [2, 20]]) == 10000


def test_largest_product_short():
    assert largest_product([[3, 8], [4, 10], [10, 50]]) == 500
