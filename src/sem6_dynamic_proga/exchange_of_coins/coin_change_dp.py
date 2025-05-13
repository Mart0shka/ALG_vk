'''
Дан массив целых чисел coin,
где каждое число - номинал монеты и
некоторое число amount - сумма монет из массива.

Необходимо найти наименьшее количество монет,
которое в сумме дало бы amount.
Если такой комбинации нет - возвращаем -1
'''

def coin_сhange_dp(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1