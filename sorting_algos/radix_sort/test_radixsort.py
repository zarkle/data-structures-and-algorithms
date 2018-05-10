from .radixsort import radix_sort


def test_radix_sort_none():
    """Test radix sort."""
    assert radix_sort([]) == []


def test_radix_sort_one():
    """Test radix sort."""
    assert radix_sort([2099]) == [2099]


def test_radix_sort():
    """Test radix sort."""
    assert radix_sort([34, 19, 42, 2018, 0, 2005, 77, 2099]) == [0, 19, 34, 42, 77, 2005, 2018, 2099]


def test_radix_sort_repeat():
    """Test radix sort."""
    assert radix_sort([34, 56, 34, 1, 1978, 10]) == [1, 10, 34, 34, 56, 1978]
