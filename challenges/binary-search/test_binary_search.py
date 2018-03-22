import binary_search

def test_binary_search():
    assert binary_search.binary_search([4, 8, 15, 16, 23, 42], 15) == 2
    assert binary_search.binary_search([11, 22, 33, 44, 55, 66, 77], 90) == -1
    assert binary_search.binary_search([1, 8, 16, 32, 54, 68, 74, 83, 95, 102, 146, 185, 190], 185) == 11
