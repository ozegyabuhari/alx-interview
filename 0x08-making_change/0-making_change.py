#!/usr/bin/python3
"""Given a pile of coins of different values,
    determine the fewest number of coins needed to meet
    a given amount total.
"""
import sys


def makeChange(coins, total):
    """ fewest number of coins needed to meet total """
    if total <= 0:
        return 0
    # sort the coins in descending order
    coins.sort(reverse=True)
    dp = 0
    for coin in coins:
        if total <= 0:
            break
        temp = total // coin
        dp += temp
        total -= (temp * coin)
    if total != 0:
        return -1
    return dp
