from .string_unique_char import unique_char


def test_unique_char_false():
    assert unique_char('The quick brown fox jumps over the lazy dog') is False
    assert unique_char('Donald the duck') is False
    assert unique_char('1a2b3C 4!g1i*?') is False



def test_unique_char_true():
    assert unique_char('I love cats') is True
    assert unique_char('abc def GHI Jkl mNop qrSt') is True
    assert unique_char('1a2b3C 4!gi*?') is True
