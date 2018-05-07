from mergesort import mergesort


def test_merge_sort_one():
    """Test merge sort."""
    assert mergesort([2099]) == [2099]


def test_merge_sort():
    """Test merge sort."""
    assert mergesort([34, 19, 42, -9, 2018, 0, 2005, 77, 2099]) == [-9, 0, 19, 34, 42, 77, 2005, 2018, 2099]


def test_merge_sort_even():
    """Test merge sort."""
    assert mergesort([34, 56, 12, 1, 1978, 10]) == [1, 10, 12, 34, 56, 1978]
