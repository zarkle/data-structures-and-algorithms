from matrix_rotate import matrix_rotate

def test_matrix_rotate():
    assert matrix_rotate([ [1, 1, 1], [2, 2, 2], [3, 3, 3] ]) == [ [3, 2, 1], [3, 2, 1], [3, 2, 1] ]
    assert matrix_rotate([ [3, 2, 1], [3, 2, 1], [3, 2, 1] ]) == [ [3, 3, 3], [2, 2, 2], [1, 1, 1] ]
