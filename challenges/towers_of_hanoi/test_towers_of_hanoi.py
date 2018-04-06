from .towers_of_hanoi import towers_of_hanoi


def test_towers_of_hanoi_two():
    assert towers_of_hanoi(2) == (3, [1, 2])


def test_towers_of_hanoi_three():
    assert towers_of_hanoi(3) == (7, [1, 2, 3])


def test_towers_of_hanoi_seven():
    assert towers_of_hanoi(7) == (127, [1, 2, 3, 4, 5, 6, 7])


def test_towers_of_hanoi_ten():
    assert towers_of_hanoi(10) == (1023, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
