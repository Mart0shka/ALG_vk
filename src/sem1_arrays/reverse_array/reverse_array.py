"""
Дан массив целых чисел.
Необходимо развернуть его.
Сделать это надо за линейное время без
дополнительных аллокаций памяти
"""

def reverse_array(arr: list):
    left, right = 0, len(arr)-1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left+=1
        right-=1
    return arr