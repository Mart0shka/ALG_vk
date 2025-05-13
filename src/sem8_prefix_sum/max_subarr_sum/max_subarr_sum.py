'''
Дан массив целых чисел arr и число k.
Требуется найти максимальную сумму
среди всех возможных подмассивов
длины k.
'''

def max_subarray_sum(arr, k):
    if len(arr) < k:
        return None

    current_sum = sum(arr[:k])
    max_sum = current_sum

    for i in range(k, len(arr)):
        current_sum = current_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, current_sum)

    return max_sum