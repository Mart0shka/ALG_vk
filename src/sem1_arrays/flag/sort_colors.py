"""
Дан массив состоящий из нулей, единиц и двоек.
Необходимо его отсортировать за линейное время
"""

def sort_colors(arr: list):
    left, mid, right = 0, 0, len(arr)-1
    while mid<=right:
        if arr[mid]==0:
            arr[left], arr[mid] = arr[mid], arr[left]
            left+=1
            mid+=1
        elif arr[mid]==2:
            arr[right], arr[mid] = arr[mid], arr[right]
            right -= 1
        else:
            mid+=1
    return arr