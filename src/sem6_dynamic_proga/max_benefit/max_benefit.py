'''
Дан массив целых чисел. Каждое число - стоимость акции.
Нам нужно купить максимально дешево, а продать максимально дорого.
Сделать это надо за O(n)

'''


def max_benefit(prices):
    if not prices:
        return 0

    profit = 0
    min_price = prices[0]

    for current_price in prices[1:]:
        profit = max(profit, current_price - min_price)
        min_price = min(current_price, min_price)

    return profit