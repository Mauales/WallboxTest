import pytest
from Wallbox.FunctionsToTest.function3 import *

VECTOR_1 = [1]*10
VECTOR_2 = [0]*10
VECTOR_3 = [0,0,1,0,1,0,1,0]
VECTOR_4 = [0,1,1,0,1,0,1,0]
VECTOR_5 = [0,1,0,0,1,0,1,0]
VECTOR_6 = [0,1,0,1,1,0,1,0]
VECTOR_7 = [0,1,0,1,0,0,1,0]
VECTOR_8 = [0,1,0,1,0,1,1,0]
VECTOR_9 = [0,1,0,1,0,1,0,0]

@pytest.mark.parametrize("a,expected", [
    (VECTOR_1, 5),
    (VECTOR_2, 5),
    (VECTOR_3, 1),
    (VECTOR_4, 2),
    (VECTOR_5, 3),
    (VECTOR_6, 4),
    (VECTOR_7, 3),
    (VECTOR_8, 2),
    (VECTOR_9, 1)
])

def test_minimumConversionsToBeInterspersed(a, expected):
    assert minimumConversionsToBeInterspersed(a) == expected

def test_minimumConversionsToBeInterspersed_Exception():
    with pytest.raises(Exception):
        minimumConversionsToBeInterspersed([])