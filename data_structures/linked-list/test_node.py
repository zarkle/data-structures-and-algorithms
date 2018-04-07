import pytest
from node import Node

def test_make_invalid_node():
    """Test that a instantiating a new Node without a value will raise an error"""
    with pytest.raises(TypeError) as err:
        Node(None)
    assert str(err.value) == 'Must pass a value'
