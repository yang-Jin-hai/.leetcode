#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        for v in nums:
            if v != val:
                nums[j] = v
                j += 1
        return j
# @lc code=end

