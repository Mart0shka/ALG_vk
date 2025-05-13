from max_subarr_sum import max_subarray_sum

def test_max_subarray_sum_basic():
    arr = [1, 2, 3, 4, 5]
    k = 2
    assert max_subarray_sum(arr, k) == 9  # [4, 5]

def test_max_subarray_sum_whole_array():
    arr = [5, -1, 3]
    k = 3
    assert max_subarray_sum(arr, k) == 7

def test_max_subarray_sum_uniform():
    arr = [7, 7, 7, 7]
    k = 3
    assert max_subarray_sum(arr, k) == 21

