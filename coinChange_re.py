"""
Quest:
    You are given coins of different denominations and a total amount of money amount.
    Write a function to compute the fewest number of coins that you need to make up that amount.
    If that amount of money cannot be made up by any combination of the coins, return -1.

    Example 1:
    Input: coins = [1, 2, 5], amount = 11
    Output: 3
    Explanation: 11 = 5 + 5 + 1

    Example 2:
    Input: coins = [2], amount = 3
    Output: -1
    Note:
    You may assume that you have an infinite number of each kind of coin.

Solution:
    - sort the coin array, then start from the largest?
    - no, because this is not real coins [1, 5, 10, 50, 100] like this, so we cannot use greedy algorithm
    - for a list [] of length = amount, each list[i] represent the least coins we need to reach the total i amount
        then for the next list[i+1], we could use dp to search 0 - i and get the result
"""


class Solution:
    def coinChange(self, coins: 'List[int]', amount: 'int') -> 'int':
        MAX = float('inf')  # here MAX means no solution to reach the amount i
        dp = [0] + [MAX] * amount

        for i in range(1, amount+1):
            dp[i] = min([dp[i-c] if i - c >= 0 else MAX for c in coins]) + 1

        return dp[amount] if dp[amount] != MAX else -1


test = Solution()
coins = [2]
amount = 3
print(test.coinChange(coins, amount))