'''
Дан массив целых чисел coin,
где каждое число - номинал монеты и
некоторое число amount - сумма монет из массива.

Необходимо найти наименьшее количество монет,
которое в сумме дало бы amount.
Если такой комбинации нет - возвращаем -1
'''


def coin_сhange(coins, amount, cache=None):
    if cache is None:
        cache = {}

    if amount == 0:
        return 0
    if amount < 0:
        return -1

    if amount in cache:
        return cache[amount]

    min_сoins = float('inf')

    for coin in coins:
        res = coin_сhange(coins, amount - coin, cache)
        if res >= 0 and res < min_сoins:
            min_сoins = res + 1

    if min_сoins == float('inf'):
        cache[amount] = -1
    else:
        cache[amount] = min_сoins

    return cache[amount]