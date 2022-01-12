#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_d, res = float('inf'), None
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue
            j, k = i+1, len(nums)-1    
            while j<k:
                s = n + nums[j] + nums[k]
                if s > target:
                    k -= 1
                    d = s - target
                elif s < target:
                    j += 1
                    d = target - s
                else:
                    return target
                if d < min_d:
                    min_d, res = d, s
        return res

# @lc code=end

