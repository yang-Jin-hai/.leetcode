#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        while low<=high:
            mid = (low+high)>>1
            v = nums[mid]
            if v == target:
                return mid
            elif v < target:
                low = mid + 1
            else:
                high = mid - 1
        return low

        
# @lc code=end

