# test_quick_sort.py
import pytest
from quick_sort import quick_sort

def test_sort_basic():
    assert quick_sort([3, 1, 4, 1, 5, 9, 2]) == [1, 1, 2, 3, 4, 5, 9]

def test_sort_empty():
    assert quick_sort([]) == []

def test_sort_single_element():
    assert quick_sort([42]) == [42]

def test_sort_sorted():
    assert quick_sort([1, 2, 3]) == [1, 2, 3]

def test_sort_reverse():
    assert quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_sort_negative():
    assert quick_sort([0, -1, -3, 8]) == [-3, -1, 0, 8]

def test_invalid_input_not_list():
    with pytest.raises(TypeError):
        quick_sort("not a list")

def test_invalid_input_non_int_elements():
    with pytest.raises(TypeError):
        quick_sort([1, "a", 3])
