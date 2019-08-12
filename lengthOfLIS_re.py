"""
Quest:
    Given an unsorted array of integers, find the length of longest increasing subsequence.

    Example:
    Input: [10,9,2,5,3,7,101,18]
    Output: 4
    Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

    Note:
    There may be more than one LIS combination, it is only necessary for you to return the length.
    Your algorithm should run in O(n2) complexity.
    Follow up: Could you improve it to O(n log n) time complexity?

Solution:
    - jus use binary search (log n)
    - the idea is: find all the IS in nums with length i+1, and store the least tail into res[i]
        that's what res contains. So in the end the res may not contain the true LIS, but the length is the same
"""

class Solution:
    def lengthOfLIS(self, nums: 'list[int]') -> 'int':
        if not nums:
            return 0

        res = []
        for i in nums:
            pos = self.helper(res, i)
            if pos == len(res):
                res.append(i)
            else:
                res[pos] = i

        return len(res)

    # find the position in res, if dont have it, return the nearest right index
    def helper(self, res, i):
        l, r = 0, len(res) - 1
        while l <= r:
            mid = (l + r) >> 1
            if res[mid] == i:
                return mid
            elif res[mid] < i:
                l = mid + 1
            else:
                r = mid - 1

        return l


test = Solution()
nums = [10,9,2,5,3,7,101,18]
print(test.lengthOfLIS(nums))