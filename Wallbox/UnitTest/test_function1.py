import pytest
from Wallbox.FunctionsToTest.function1 import *

VECTOR_1 = [1,2,3,4,5,6]
VECTOR_2 = [6,5,4,3,2,1]
VECTOR_3 = [7,8,9]
VECTOR_4 = []

@pytest.mark.parametrize("a,b,expected", [
    (VECTOR_1, VECTOR_2, "Duplicate integer: 6"),
    (VECTOR_2, VECTOR_1, "Duplicate integer: 1"),
    (VECTOR_1, VECTOR_3, "No duplicates found")
])


def test_findFirstDuplicate(a, b, expected):
    assert findFirstDuplicate(a, b) == expected


@pytest.mark.parametrize("a,b", [
    (VECTOR_1, VECTOR_4),
    (VECTOR_4, VECTOR_1)
])

def test_findFirstDuplicate_Exception(a, b):
    with pytest.raises(Exception):
        findFirstDuplicate(a,b)