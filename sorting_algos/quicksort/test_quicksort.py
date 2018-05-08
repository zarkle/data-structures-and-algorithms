from .quicksort import quick_sort


def test_quick_sort_none():
    """Test quick sort."""
    assert quick_sort([]) == []


def test_quick_sort_one():
    """Test quick sort."""
    assert quick_sort([2099]) == [2099]


def test_quick_sort():
    """Test quick sort."""
    assert quick_sort([34, 19, 42, -9, 2018, 0, 2005, 77, 2099]) == [-9, 0, 19, 34, 42, 77, 2005, 2018, 2099]


def test_quick_sort_repeat():
    """Test quick sort."""
    assert quick_sort([34, 56, 34, 1, 1978, 10]) == [1, 10, 34, 34, 56, 1978]
