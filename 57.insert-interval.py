#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s, e = newInterval
        l, r = [], []
        for x in intervals:
            if x[1] < s:
                l.append(x)
            elif x[0] > e:
                r.append(x)
            else:
                s, e = min(s, x[0]), max(e, x[1])
        return l + [[s, e]] + r

# @lc code=end

