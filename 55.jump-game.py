#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums)-1
        for i in range(len(nums))[::-1]:
            if i+nums[i] >= target:
                target = i
        return not target
        # end = 0
        # for i, x in enumerate(nums):
        #     if end < i:
        #         return False
        #     end = max(end, i+x)
        # return True

            
# @lc code=end

