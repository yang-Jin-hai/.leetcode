#
# @lc app=leetcode.cn id=1991 lang=python3
#
# [1991] 找到数组的中间位置
#

# @lc code=start
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total, s = sum(nums), 0
        for i, num in enumerate(nums):
            total -= num
            if total == s:
                return i
            s += num
        return -1
# @lc code=end

