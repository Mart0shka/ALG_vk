"""
В небольшом зоопарке есть некоторое количество животных.
Каждое животное потребляет какой-то объем еды, выраженный в целочисленном значении.
Например, еноту нужна 1-порция еды, зебре 2, пантере 3, льву 4, жирафу 8 и т.д.
Каждый день, смотритель зоопарка привозит еду такими же порциями. То есть за раз он
привозит 8, 3, 9, 1, 7. Порция на 8 может накормить одно животное один раз.
То есть такая порция может накормить либо енота, либо льва, либо жирафа, но не может накормить,
например зебру и енота. Только кого-то одного.

Надо написать функцию, которая определит, сколько из переданных животных может накормить заданное количество еды.
"""

def merge(arr1, arr2):
    res, p1, p2 = [], 0, 0
    while p1<len(arr1) and p2<len(arr2):
        if arr1[p1] < arr2[p2]:
            res.append(arr1[p1])
            p1+=1
        else:
            res.append(arr2[p2])
            p2+=1

    while p1<len(arr1):
        res.append(arr1[p1])
        p1+=1

    while p2 < len(arr2):
        res.append(arr2[p2])
        p2 += 1

    return res

def merge_sort(arr):
    if len(arr)<2:
        return arr

    mid = len(arr)//2
    left_side = arr[0 : mid]
    right_side = arr[mid : len(arr)]

    return merge(merge_sort(left_side), merge_sort(right_side))

def feed_animals(animals, food):
    if len(animals) == 0 or len(food)==0:
        return 0

    animals = merge_sort(animals)
    food = merge_sort(food)

    counter = 0
    for f in food:
        if f>=animals[counter]:
            counter += 1

        if counter == len(animals):
            break

    return counter
