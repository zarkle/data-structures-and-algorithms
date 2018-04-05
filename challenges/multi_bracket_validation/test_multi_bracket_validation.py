from .multi_bracket_validation import multi_bracket_validation


def test_multi_bracket_validation_one_round_true():
    assert multi_bracket_validation('(abc)') is True


def test_multi_bracket_validation_one_square_true():
    assert multi_bracket_validation('[abc]') is True


def test_multi_bracket_validation_one_curly_true():
    assert multi_bracket_validation('{{abc}}') is True


def test_multi_bracket_validation_two_true():
    assert multi_bracket_validation('{{{{abc}}}}') is True


def test_multi_bracket_validation_three_true():
    assert multi_bracket_validation('()([abc])') is True


def test_multi_bracket_validation_one_false():
    assert multi_bracket_validation('(abc]') is False


def test_multi_bracket_validation_two_false():
    assert multi_bracket_validation('([abc)') is False


def test_multi_bracket_validation_three_false():
    assert multi_bracket_validation('[[[abc]]') is False


def test_multi_bracket_validation_three_round_false():
    assert multi_bracket_validation('((abc)))') is False
