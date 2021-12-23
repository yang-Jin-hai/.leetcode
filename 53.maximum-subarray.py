#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # m = len(nums)
        # dp = m*[nums[0]]
        # for i in range(1, m):
        #     dp[i]=max(nums[i], nums[i]+dp[i-1])
        # return max(dp)

        cur = res = nums[0]
        for i in nums[1:]:
            cur = max(i, cur+i)
            res = max(res, cur)
        return res
# @lc code=end

