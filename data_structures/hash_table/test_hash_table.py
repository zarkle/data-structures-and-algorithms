"""Test hash table class."""
from .hash_table import HashTable as HT


def test_hash_table_hash_key_single():
    """Test a hash table hashkey function."""
    hash = HT()
    assert hash._hash_key('b') == 98


def test_hash_table_set():
    """Test hash table set function."""
    hash = HT()
    hash.set('key', {'abc': 'def'})
    assert hash.buckets[329].head.val['key'] == {'abc': 'def'}


def test_hash_table_get():
    """Test hash table get function."""
    hash = HT()
    hash.set('key', 123)
    assert hash.get('key') == [123]


def test_hash_table_remove():
    """Test hash table remove function."""
    hash = HT()
    hash.set('key', {'abc': 'def'})
    hash.remove('key')
    assert hash.buckets[329].head is None
    assert hash.get('key') == []


