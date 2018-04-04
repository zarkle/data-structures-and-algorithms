import multi_bracket_validation


def test_multi_bracket_validation_one_true():
    assert multi_bracket_validation('(abc)') is True


def test_multi_bracket_validation_two_true():
    assert multi_bracket_validation('\{\{abc\}\}') is True


def test_multi_bracket_validation_three_true():
    assert multi_bracket_validation('()([\{abc\}])') is True


def test_multi_bracket_validation_one_false():
    assert multi_bracket_validation('(abc]') is False


def test_multi_bracket_validation_two_false():
    assert multi_bracket_validation('([abc)') is False


def test_multi_bracket_validation_three_false():
    assert multi_bracket_validation('[[[abc]]') is False
