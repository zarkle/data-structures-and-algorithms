from .towers_of_hanoi import towers_of_hanoi


def test_towers_of_hanoi_two():
    assert towers_of_hanoi(2) == (3, [2, 1], [], [])


def test_towers_of_hanoi_three():
    assert towers_of_hanoi(3) == (7, [3, 2, 1], [], [])


def test_towers_of_hanoi_seven():
    assert towers_of_hanoi(7) == (127, [7, 6, 5, 4, 3, 2, 1], [], [])


def test_towers_of_hanoi_ten():
    assert towers_of_hanoi(10) == (1023, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [], [])
