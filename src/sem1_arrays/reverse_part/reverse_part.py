"""
Дан массив целых чисел.
Необходимо повернуть (сдвинуть) справа налево часть массива, которая
указана вторым параметром.
Сделать это надо за линейное время без дополнительных аллокаций

Исходный массив: 1, 2, 3, 4, 5, 6, 7
k = 3
Результат: 5, 6, 7, 1, 2, 3, 4
"""

def reverse_arr(arr: list, st: int, en: int):
    left, right = st, en
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left+=1
        right-=1
    return arr

def solution(arr: list, k: int):
    n = len(arr)
    arr = reverse_arr(arr,0, n-1)
    arr = reverse_arr(arr, 0, k%n-1)
    arr = reverse_arr(arr, k%n, n-1)
    return arr