#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l <= r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            if s > target:
                r -= 1
            else:
                l += 1
# @lc code=end

