import pytest
import sys
sys.path.append("./")
from src.sorting.sorting import insertion_sort, selection_sort, heap_sort

@pytest.fixture(params=[insertion_sort, selection_sort, heap_sort])
def sort_function(request):
    return request.param

@pytest.fixture
def sample_lists():
    return [
        [],
        [1],
        [1, 2],
        [2, 1],
        [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],
        [3, 3, 3, 1, 1, 2, 2],
        [-5, 0, -3, 2, -1, 10, -7],
        [1000000, 10, 100000, 1000, 100],
    ]

def test_sorting(sort_function, sample_lists):
    for unsorted_list in sample_lists:
        sorted_list = sorted(unsorted_list)
        result = unsorted_list.copy()
        sort_function(result)
        assert result == sorted_list, f"Failed for input: {unsorted_list}"

@pytest.mark.parametrize("size", [100, 1000, 10000])
def test_random_large_list(sort_function, size):
    import random
    random.seed(42)
    input_list = [random.randint(-1000, 1000) for _ in range(size)]
    expected = sorted(input_list)
    result = input_list.copy()
    sort_function(result)
    assert result == expected, f"Failed for random list of size {size}"

def test_original_list_unchanged(sort_function):
    original = [5, 2, 8, 12, 1, 6]
    input_list = original.copy()
    sort_function(input_list)
    assert original == [5, 2, 8, 12, 1, 6], "Original list was modified"
    assert input_list == [1, 2, 5, 6, 8, 12], "Sorting failed"
