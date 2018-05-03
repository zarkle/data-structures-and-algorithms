from .repeated_word import repeated_word



def test_repeated_word_one():
    """Test repeated word function."""
    assert repeated_word('Once twice once') == 'once'


def test_repeated_word_two():
    """Test repeated word function."""
    assert repeated_word('Once upon a time, there was a student who plagarized') == 'a'


def test_repeated_word_three():
    """Test repeated word function."""
    assert repeated_word('It was a queer sultry summer the summer they electrocuted the Rosenberg') == 'summer'
