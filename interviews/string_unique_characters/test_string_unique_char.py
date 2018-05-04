from .string_unique_char import unique_char


def test_unique_char_one():
    # assert unique_char('The quick brown fox jumps over the lazy dog') is False
    assert unique_char('I love cats') is True
    # assert unique_char('Donald the duck') is False
