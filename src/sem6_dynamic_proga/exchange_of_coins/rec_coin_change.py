'''
Дан массив целых чисел coin,
где каждое число - номинал монеты и
некоторое число amount - сумма монет из массива.

Необходимо найти наименьшее количество монет,
которое в сумме дало бы amount.
Если такой комбинации нет - возвращаем -1
'''

def rec_coin_change(coins, amount):
    if amount == 0:
        return 0
    if amount < 0:
        return -1

    min_coins = float('inf')

    for coin in coins:
        res = rec_coin_change(coins, amount-coin)

        if (res >= 0 and res<min_coins):
            min_coins = res+1

    if min_coins == float('inf'):
        return -1

    return min_coins