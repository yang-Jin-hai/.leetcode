#
# @lc app=leetcode.cn id=713 lang=python3
#
# [713] 乘积小于K的子数组
#

# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = res = 0
        m = len(nums)
        p = 1
        for r in range(m):
            p *= nums[r]
            while p >= k and l <= r:
                p /= nums[l]
                l += 1
            res += r - l + 1                
        return res

# @lc code=end

