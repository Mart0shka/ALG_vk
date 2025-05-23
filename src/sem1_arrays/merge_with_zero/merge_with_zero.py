"""
Дано два отсортированных массива. Необходимо
написать функцию которая объединит эти два массива
в один отсортированный.
Первый массив имеет размер, равный
результирующиму массиву, значения в конце равны
нулям. Мы не должны создавать третий массив.
"""

def merge(arr1: list, arr2: list):
    pointer1 = len(arr1) - len(arr2) - 1
    pointer2 = len(arr2) - 1
    pointer3 = len(arr1) - 1

    while pointer2 >= 0:
        if pointer1>=0 and arr1[pointer1] > arr2[pointer2]:
            arr1[pointer3] = arr1[pointer1]
            pointer1 -= 1
        else:
            arr1[pointer3] = arr2[pointer2]
            pointer2 -= 1
        pointer3 -= 1

    return arr1
