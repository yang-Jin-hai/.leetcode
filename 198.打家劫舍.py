#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        pre = nums[0]
        cur = max(nums[:2])
        for i in range(2, len(nums)):
            pre, cur = cur, max(cur, pre+nums[i])
        return cur
        # @lru_cache(None)
        # def dfs(i):
        #     if i == 0: return nums[0]
        #     if i == 1: return max(nums[0], nums[1])
        #     return max(dfs(i-1), dfs(i-2)+nums[i])
        # return dfs(len(nums)-1)
# @lc code=end

