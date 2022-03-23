#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        m = len(nums)
        s = sum(nums)
        target += s
        if target & 1 or target < 0: return 0
        target >>= 1 
        dp = [0] * (target+1)
        dp[0] = 1
        for i in range(m):
            for j in range(nums[i], target+1)[::-1]:
                dp[j] += dp[j-nums[i]]
        return dp[-1]
# @lc code=end

