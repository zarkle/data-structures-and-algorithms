from .multi_bracket_validation import multi_bracket_validation


def test_multi_bracket_validation_one_round_true():
    """Test for multi-bracket validity"""
    assert multi_bracket_validation('(abc)') is True


def test_multi_bracket_validation_one_square_true():
    """Test for multi-bracket validity"""
    assert multi_bracket_validation('[abc]') is True


def test_multi_bracket_validation_one_curly_true():
    """Test for multi-bracket validity"""
    assert multi_bracket_validation('{{abc}}') is True


def test_multi_bracket_validation_two_true():
    """Test for multi-bracket validity"""
    assert multi_bracket_validation('{{{{abc}}}}') is True


def test_multi_bracket_validation_three_true():
    """Test for multi-bracket validity"""
    assert multi_bracket_validation('()([abc])') is True


def test_multi_bracket_validation_one_false():
    """Test for multi-bracket validity"""
    assert multi_bracket_validation('(abc]') is False


def test_multi_bracket_validation_two_false():
    """Test for multi-bracket validity"""
    assert multi_bracket_validation('([abc)') is False


def test_multi_bracket_validation_three_false():
    """Test for multi-bracket validity"""
    assert multi_bracket_validation('[[[abc]]') is False


def test_multi_bracket_validation_three_round_false():
    """Test for multi-bracket validity"""
    assert multi_bracket_validation('((abc)))') is False
