from selection import selectionsort


def test_selection_sort_one():
    """Test selection sort."""
    assert selectionsort([2099]) == [2099]


def test_selection_sort():
    """Test selection sort."""
    assert selectionsort([34, 19, 42, -9, 2018, 0, 2005, 77, 2099]) == [-9, 0, 19, 34, 42, 77, 2005, 2018, 2099]


def test_selection_sort_even():
    """Test selection sort."""
    assert selectionsort([34, 56, 12, 1, 1978, 10]) == [1, 10, 12, 34, 56, 1978]
