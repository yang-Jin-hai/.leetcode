#
# @lc app=leetcode.cn id=724 lang=python3
#
# [724] 寻找数组的中心下标
#

# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        s = 0
        for i, num in enumerate(nums):
            s += num
            if s - num == total - s:
                return i
        return -1
        # (1)
        # s = 0
        # total = sum(nums)
        # m = len(nums)
        # record = {-1:0, m: total}
        # for i, num in enumerate(nums):
        #     s += num
        #     record[i] = s
        # for i, num in enumerate(nums):
        #     if record[i] - num == total - record[i]:
        #         return i
        # return -1

# @lc code=end

