"""
Quest:
    Given an array of non-negative integers, you are initially positioned at the first index of the array.
    Each element in the array represents your maximum jump length at that position.
    Determine if you are able to reach the last index.

    Example 1:
    Input: [2,3,1,1,4]
    Output: true
    Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

    Example 2:
    Input: [3,2,1,0,4]
    Output: false
    Explanation: You will always arrive at index 3 no matter what. Its maximum
                 jump length is 0, which makes it impossible to reach the last index.

Solution:
    - recursion (use helper), search from end to begin
"""


class Solution:
    def canJump(self, nums: 'List[int]') -> 'bool':
        if not nums:
            return False

        n = len(nums) - 1
        if self.helper(nums, n):
            return True
        else:
            return False

    def helper(self, nums, n):
        if n == 0:
            return True

        for i in range(n-1, -1, -1):
            if nums[i] >= (n-i):
                return self.helper(nums, i)


test = Solution()
x = [3,2,1,0,4]
print(test.canJump(x))