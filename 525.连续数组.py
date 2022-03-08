#
# @lc app=leetcode.cn id=525 lang=python3
#
# [525] 连续数组
#

# @lc code=start
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res = 0
        s = 0
        record = {0: -1}
        for i, num in enumerate(nums):
            if num == 0:
                s -= 1
            else:
                s += 1
            if s in record:
                res = max(res, i-record[s])
            else:
                record[s] = i
        return res
# @lc code=end

