import pytest
import shift_array

def test_insertShiftArray():
    assert shift_array.insertShiftArray([1, 2, 3, 4], 6) == [1, 2, 6, 3, 4]
    assert shift_array.insertShiftArray([5, 4, 3, 2, 1], 10) == [5, 4, 10, 3, 2, 1]
    assert shift_array.insertShiftArray([1, 10], 5) == [1, 5, 10]
