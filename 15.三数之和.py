#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[l] + nums[r]
                if s + num == 0:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    while l < len(nums)-1 and nums[l] == nums[l-1]:
                        l += 1
                elif s + num > 0:
                    r -= 1
                else:
                    l += 1
        return res 
# @lc code=end

