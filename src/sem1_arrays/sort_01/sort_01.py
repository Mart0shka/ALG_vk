'''
Дан массив, содержащий только 0 и 1. Напишите функцию,
которая сортирует его так, чтобы все нули оказались в
начале, а все единички - в конце. Решение должно быть
in-place.
'''

def sort(arr: list):
    left, right = 0, len(arr)-1
    while left<right:
        if arr[left] == 1:
            arr[left], arr[right] = arr[right], arr[left]
            right-=1
        else:
            left+=1
    return arr