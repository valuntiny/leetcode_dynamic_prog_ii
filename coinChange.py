'''
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
'''


class Solution:
    def coinChange(self, coins: 'List[int]', amount: 'int') -> 'int':
        MAX = float("inf")
        dp = [0] + [MAX] * amount

        for i in range(1, amount + 1):
            tmp = []
            for c in coins:
                if i - c >= 0:
                    tmp.append(dp[i - c])
                else: tmp.append(MAX)
            dp[i] = min(tmp) + 1

        return [dp[amount], -1][dp[amount] == MAX]

test = Solution()
coins = [1, 2, 5]
amount = 11
print(test.coinChange(coins, amount))