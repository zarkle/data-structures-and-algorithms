import pytest
from fifo_animal_shelter import AnimalShelter as AS


@pytest.fixture
def empty_queue():
    """create an empty queue"""
    return AS()


@pytest.fixture
def short_queue():
    """create a short queue"""
    return AS(['dog', 'cat', 'dog', 'cat'])


@pytest.fixture
def ddc_queue():
    """create a dog, dog, cat queue"""
    return AS(['dog', 'dog', 'cat'])
