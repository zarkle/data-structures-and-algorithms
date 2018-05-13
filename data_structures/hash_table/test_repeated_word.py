from .repeated_word import repeated_word
import pytest


def test_repeated_word_error():
    """Test repeated word raises error."""
    with pytest.raises(TypeError) as err:
        repeated_word(1234567890)
        assert err.value == 'Input must be string.'


def test_repeated_word_one():
    """Test repeated word function."""
    assert repeated_word('Once upon a time there was a brave princess who') == 'a'


def test_repeated_word_two():
    """Test repeated word function."""
    assert repeated_word('Once twice once') == 'once'


def test_repeated_word_three():
    """Test repeated word function."""
    assert repeated_word('It was a queer sultry summer the summer they electrocuted the Rosenberg') == 'summer'
