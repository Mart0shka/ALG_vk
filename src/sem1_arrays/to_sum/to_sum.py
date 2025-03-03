"""
Дан отсортированный по возрастанию
массив целых чисел и некоторое число target
Необходимо найти два числа в массиве,
которые в сумме дают заданное значение
target, и вернуть их индексы.
"""

def twoSum(arr: list, target: int):
    left, right = 0, len(arr)-1
    while left < right:
        sum = arr[left] + arr[right]
        if sum == target:
            return left, right
        if sum < target:
            left+=1
        else:
            right-=1
    return None