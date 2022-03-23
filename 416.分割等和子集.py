#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target & 1: return False
        target >>= 1
        # @lru_cache(None)
        # def dfs(i, target):
        #     if target == 0: return True
        #     if i < 0: return False
        #     return dfs(i-1, target) or dfs(i-1, target-nums[i])
        # return dfs(len(nums)-1, target)
        dp = [False] * (target+1)
        for i in range(len(nums)):
            dp[0] = True
            for j in range(1, target+1)[::-1]:
                dp[j] = dp[j] or (j >= nums[i] and dp[j-nums[i]])
        return dp[-1]
# @lc code=end

