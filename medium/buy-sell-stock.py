"""
Q - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
A - 
"""

from typing import List

# Smart Way


def max_profit_1(prices: List[int]) -> int:
    buy = 0
    sell = 1
    max_profit = 0
    while sell < len(prices):
        profit = prices[sell] - prices[buy]

        if prices[buy] < prices[sell]:
            max_profit = max(max_profit, profit)
        else:
            buy = sell
        sell += 1
    return max_profit

# Brute Force Recursive


def find_max_profit(max_profit, prices):
    if len(prices) <= 1:
        print(f'returning {max_profit}')
        return max_profit

    buy = prices[0]
    max_sell = max([sell for sell in prices[1:]])
    max_profit = max(max_profit, max_sell-buy)

    print(f'checking {prices}')
    print(f'max profit so far is {max_profit}')

    return find_max_profit(max_profit, prices[1:])


def max_profit_2(prices: List[int]) -> int:
    if len(prices) == 1:
        return 0

    return find_max_profit(0, prices)


prices_5 = [7, 1, 5, 3, 6, 4]
prices_0 = [7, 6, 4, 3, 1]

print(max_profit_1(prices_5))
