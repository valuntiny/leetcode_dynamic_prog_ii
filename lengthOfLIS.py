'''
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n^2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
'''


class Solution:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0

        res = []
        for i in nums:
            pos = self.binarysearch(res, i)
            if pos == len(res):
                res.append(i)
            else:
                res[pos] = i

        print(res)
        return len(res)

    def binarysearch(self, res, i):
        l, r = 0, len(res) - 1
        while l <= r:
            mid  = (l + r) >> 1
            if res[mid] < i:
                l = mid + 1
            elif res[mid] > i:
                r = mid - 1
            else:
                return mid

        return l

test = Solution()
nums = [10,9,2,5,3,7,101,18]
print(test.lengthOfLIS(nums))