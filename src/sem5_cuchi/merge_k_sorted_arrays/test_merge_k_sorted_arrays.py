from src.sem5_cuchi.merge_k_sorted_arrays.merge_k_sorted_arrays import merge_k_sorted_arrays

def test_empty_input():
    assert merge_k_sorted_arrays([]) == []

def test_single_empty_array():
    assert merge_k_sorted_arrays([[]]) == []

def test_single_array():
    assert merge_k_sorted_arrays([[1, 2, 3]]) == [1, 2, 3]

def test_multiple_arrays():
    assert merge_k_sorted_arrays([
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9]
    ]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_arrays_different_lengths():
    assert merge_k_sorted_arrays([
        [1, 3, 5, 7],
        [2, 4],
        [6, 8, 9]
    ]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_with_negative_numbers():
    assert merge_k_sorted_arrays([
        [-5, -3, 0],
        [-4, -2, 1],
        [-1, 2, 3]
    ]) == [-5, -4, -3, -2, -1, 0, 1, 2, 3]

def test_duplicate_values():
    assert merge_k_sorted_arrays([
        [1, 1, 2, 3],
        [1, 2, 2, 4],
        [3, 4, 5]
    ]) == [1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5]

def test_large_arrays():
    array1 = list(range(0, 10000, 2))
    array2 = list(range(1, 10000, 2))
    result = merge_k_sorted_arrays([array1, array2])
    assert result == sorted(array1 + array2)
    assert len(result) == len(array1) + len(array2)

def test_with_empty_arrays_mixed():
    assert merge_k_sorted_arrays([
        [1, 3, 5],
        [],
        [2, 4, 6],
        [],
        [7, 8]
    ]) == [1, 2, 3, 4, 5, 6, 7, 8]