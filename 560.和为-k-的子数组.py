#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        record = {0: 1}
        s = 0
        for num in nums:
            s += num
            if s-k in record:
                res += record[s-k]
            if s in record:
                record[s] += 1
            else:
                record[s] = 1
        return res
# @lc code=end

