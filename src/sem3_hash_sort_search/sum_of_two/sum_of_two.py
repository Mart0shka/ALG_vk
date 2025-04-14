"""
Дан не отсортированный массив целых чисел и некоторое число target.
Необходимо написать функцию, которая найдет два таких элемента в массиве,
сумма которых будет равна target
Один элемент можно использовать лишь один раз.
В случае если два таких элемента не нашлось, возвращаем пустой массив
"""

def sum_of_two(data, target):
    cache = dict()
    for i in range(len(data)):
        cache[data[i]] = i

    for i in range(len(data)):
        diff = target - data[i]
        if diff in cache.keys() and i!=cache[diff]:
            return (i, cache[diff])
    return None
