#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(1, len(nums)-1):
            low, high = 0, len(nums)-1
            if i > 1 and nums[i]==nums[i-1]:
                low = i-1
            while low<i and i<high:
                if low>0 and nums[low]==nums[low-1]:
                    low += 1
                    continue
                if high<len(nums)-1 and nums[high]==nums[high+1]:
                    high -= 1
                    continue
                s = nums[low] + nums[high] + nums[i]
                if s == 0:
                    res.append([nums[low], nums[high], nums[i]])
                    high -= 1
                    low += 1
                elif s > 0:
                    high -= 1
                else:
                    low += 1
        return res
        
# @lc code=end

