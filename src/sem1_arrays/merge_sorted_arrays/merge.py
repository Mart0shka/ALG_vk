"""
Дано два отсортированных массива. Необходимо
написать функцию которая объединит эти два массива
в один отсортированный.
"""

def merge_sorted_arrays(arr1, arr2):
    arr = []
    p1, p2 = 0,0
    while p1<len(arr1) and p2<len(arr2):
        if arr1[p1]<arr2[p2]:
            arr.append(arr1[p1])
            p1+=1
        else:
            arr.append(arr2[p2])
            p2+=1

    arr += arr1[p1:]
    arr += arr2[p2:]

    return arr
