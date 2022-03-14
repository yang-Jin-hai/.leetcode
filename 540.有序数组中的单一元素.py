#
# @lc app=leetcode.cn id=540 lang=python3
#
# [540] 有序数组中的单一元素
#

# @lc code=start
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1
        if n == 0 or nums[0] != nums[1]:
            return nums[0]
        if nums[n] != nums[n-1]:
            return nums[n]
        l, r = 1, len(nums)-2
        while l <= r:
            m = (l+r)>>1
            if nums[m] != nums[m-1] and nums[m] != nums[m+1]:
                return nums[m]
            if m & 1 == 1:
                if nums[m] != nums[m-1]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] != nums[m+1]:
                    r = m - 1
                else:
                    l = m + 1

# @lc code=end

