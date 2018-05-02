from .hash_table import HashTable as HT
from .left_join import left_join
import pytest


@pytest.fixture
def hash_table_one_syn():
    hash = HT(5)
    hash.set('fond', 'enamored')
    hash.set('wrath', 'anger')
    hash.set('diligent', 'employed')
    return hash


@pytest.fixture
def hash_table_one_ant():
    hash = HT(5)
    hash.set('fond', 'averse')
    hash.set('wrath', 'delight')
    hash.set('diligent', 'idle')
    return hash


@pytest.fixture
def hash_table_two_syn():
    hash = HT(6)
    hash.set('guide', 'usher')
    hash.set('wrath', 'anger')
    hash.set('diligent', 'employed')
    hash.set('outfit', 'garb')
    return hash


@pytest.fixture
def hash_table_two_ant():
    hash = HT(6)
    hash.set('fond', 'averse')
    hash.set('wrath', 'delight')
    hash.set('guide', 'follow')
    hash.set('flow', 'jam')
    return hash


def test_left_join_two(hash_table_two_syn, hash_table_two_ant):
    """Test left join."""
    assert left_join(hash_table_two_syn, hash_table_two_ant) == [['outfit', 'garb', 'NULL'], ['diligent', 'employed', 'NULL'], ['guide', 'usher', 'follow'], ['wrath', 'anger', 'delight']]


def test_left_join_one(hash_table_one_syn, hash_table_one_ant):
    """Test left join."""
    assert left_join(hash_table_one_syn, hash_table_one_ant) == [['wrath', 'anger', 'delight'], ['fond', 'enamored', 'averse'], ['diligent', 'employed', 'idle']]


def test_left_join_three(hash_table_one_syn, hash_table_two_ant):
    """Test left join."""
    assert left_join(hash_table_one_syn, hash_table_two_ant) == [['wrath', 'anger', 'delight'], ['fond', 'enamored', 'averse'], ['diligent', 'employed', 'NULL']]


def test_left_join_four(hash_table_two_syn, hash_table_one_ant):
    """Test left join."""
    assert left_join(hash_table_two_syn, hash_table_one_ant) == [['outfit', 'garb', 'NULL'], ['diligent', 'employed', 'idle'], ['guide', 'usher', 'NULL'], ['wrath', 'anger', 'delight']]

