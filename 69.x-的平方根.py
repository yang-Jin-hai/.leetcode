#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            m = (l+r) >> 1
            p = m * m
            if p == x:
                return m
            if p > x:
                r = m - 1
            else:
                l = m + 1
        return r
# @lc code=end

