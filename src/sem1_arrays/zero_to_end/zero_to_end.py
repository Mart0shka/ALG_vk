"""
В школе прошел экзамен по математике.
Несколько человек списали решения и были
замечены. Этим школьникам поставил 0
баллов. Задача: есть массив с оценками,
среди которых есть 0. Необходимо все
оценки, равные нулю перенести в конец
массива, чтобы все такие школьники
оказались в конце списка.
"""

def zero_to_end(arr: list):
    zero_idx, iter_idx = 0, 0
    while iter_idx < len(arr) and zero_idx < len(arr) :
        if arr[zero_idx] != 0:
            zero_idx += 1
            iter_idx += 1
        elif arr[iter_idx] == 0:
            iter_idx += 1
        elif arr[iter_idx] != 0:
            arr[zero_idx], arr[iter_idx] = arr[iter_idx], arr[zero_idx]
            zero_idx += 1

    return arr