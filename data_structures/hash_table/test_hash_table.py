"""Test hash table class."""
import pytest
from .hash_table import HashTable as HT


def test_hash_table_default():
    """Test a hash table."""
    hash = HT()
    assert hash.max_size == 1024
    assert len(hash.buckets) == 1024


def test_hash_table_given_max():
    """Test a hash table."""
    hash = HT(4)
    assert hash.max_size == 4
    assert len(hash.buckets) == 4


def test_hash_table_hash_size_error_type():
    """Test a hash table."""
    with pytest.raises(TypeError) as err:
        HT('two')
        assert err.value == 'Max size must be Integer'


def test_hash_table_hash_size_error_value():
    """Test a hash table."""
    with pytest.raises(ValueError) as err:
        HT(-2)
        assert err.value == 'Max size must be non-negative Integer'


def test_hash_table_hash_key_error():
    """Test a hash table hashkey function."""
    hash = HT()
    with pytest.raises(TypeError) as err:
        hash._hash_key(5)
        assert err.value == 'Key must be String'


def test_hash_table_hash_key_single():
    """Test a hash table hashkey function."""
    hash = HT()
    assert hash._hash_key('b') == 98


def test_hash_table_hash_key_word():
    """Test a hash table hashkey function."""
    hash = HT()
    assert hash._hash_key('key') == 329
    assert hash._hash_key('Key') == 297


def test_hash_table_set_error():
    """Test hash table set function."""
    hash = HT()
    with pytest.raises(TypeError) as err:
        hash.set(123, {'msira': 'igalp'})
        assert err.value == 'Key must be String'


def test_hash_table_set():
    """Test hash table set function."""
    hash = HT()
    hash.set('key', {'abc': 'def'})
    assert hash.buckets[329].head.val['key'] == {'abc': 'def'}


def test_hash_table_set_one_bucket():
    """Test hash table set function."""
    hash = HT(1)
    hash.set('key', 123)
    assert hash.buckets[0].head.val['key'] == 123


def test_hash_table_set_two():
    """Test hash table set function."""
    hash = HT(1)
    hash.set('whiskey', 'is cute')
    assert hash.buckets[0].head.val['whiskey'] == 'is cute'


def test_hash_table_get_error():
    """Test hash table get function."""
    hash = HT()
    with pytest.raises(TypeError) as err:
        hash.get(123)
        assert err.value == 'Key must be String'


def test_hash_table_get():
    """Test hash table get function."""
    hash = HT()
    hash.set('key', 123)
    assert hash.get('key') == 123


def test_hash_table_get_one():
    """Test hash table get function."""
    hash = HT(1)
    hash.set('abc', 'def')
    assert hash.get('abc') == 'def'


def test_hash_table_get_two():
    """Test hash table get function."""
    hash = HT(2)
    hash.set('key', {'abc': 'def'})
    assert hash.get('key') == {'abc': 'def'}


def test_hash_table_get_none():
    """Test hash table get function."""
    hash = HT(2)
    assert hash.get('key') is None


def test_hash_table_remove_error():
    """Test hash table remove function."""
    hash = HT()
    with pytest.raises(TypeError) as err:
        hash.remove(123)
        assert err.value == 'Key must be String'


def test_hash_table_remove():
    """Test hash table remove function."""
    hash = HT()
    hash.set('key', {'abc': 'def'})
    hash.remove('key')
    assert hash.buckets[329].head is None
    assert hash.get('key') is None


def test_hash_table_remove_one_bucket():
    """Test hash table remove function."""
    hash = HT(1)
    hash.set('key', 123)
    hash.remove('key')
    assert hash.buckets[0].head is None
    assert hash.get('key') is None


def test_hash_table_remove_two():
    """Test hash table remove function."""
    hash = HT(1)
    hash.set('whiskey', 'is cute')
    hash.remove('whiskey')
    assert hash.buckets[0].head is None
    assert hash.get('whiskey') is None
