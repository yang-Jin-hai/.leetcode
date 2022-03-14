#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for interval in intervals[1:]:
            l, r = interval
            if l <= res[-1][1]:
                res[-1][1] = max(r, res[-1][1])
            else:
                res.append(interval)
        return res
# @lc code=end

