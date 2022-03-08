#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = 100000
        l = r = 0
        s = nums[0]
        while l <= r and r < len(nums):
            if s >= target:
                res = min(res, r-l+1)
                s -= nums[l]
                l += 1
            else:
                r += 1
                if r < len(nums):
                    s += nums[r]
        return res if res < 100000 else 0
# @lc code=end

