"""
Quest:
    A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
    The robot can only move either down or right at any point in time.
    The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
    How many possible unique paths are there?

    Note: m and n will be at most 100.

    Example 1:
    Input: m = 3, n = 2
    Output: 3
    Explanation:
    From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
    1. Right -> Right -> Down
    2. Right -> Down -> Right
    3. Down -> Right -> Right

    Example 2:
    Input: m = 7, n = 3
    Output: 28

Solution:
    - treat it as a matrix
"""


class Solution:
    def uniquePaths(self, m: 'int', n: 'int') -> 'int':
        # the traversing mxn matrix
        mat = [[1 for i in range(n)] for j in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                mat[i][j] = mat[i-1][j] + mat[i][j-1]

        return mat[m-1][n-1]


test = Solution()
m = 7
n = 3
print(test.uniquePaths(m,n))