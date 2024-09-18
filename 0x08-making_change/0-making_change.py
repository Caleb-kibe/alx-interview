#!/usr/bin/python3

def makeChange(coins, total):
    """ Determine the fewest number of coins needed
        to meet a given amount total
    """
    if total <= 0:
        return 0

    # Create a dp array to store the minimum number of coins for each amount up to 'total'
    dp = [float('inf')] * (total + 1)

    # Base case: 0 coins are needed to make a total of 0
    dp[0] = 0

    # Fill the dp array by trying each coin denomination for each amount
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still 'inf', it means it's not possible to make the total with the given coins
    return dp[total] if dp[total] != float('inf') else -1
