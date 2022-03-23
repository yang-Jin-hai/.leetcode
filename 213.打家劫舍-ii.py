#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        def dp(start, end):
            pre, cur = nums[start], max(nums[start:start+2])
            for i in range(start+2, end):
                pre, cur = cur, max(pre+nums[i], cur)
            return cur
        return max(dp(0, len(nums)-1), dp(1, len(nums)))
    
# @lc code=end

