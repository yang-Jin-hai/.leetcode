#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        r2i = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        # s = s.replace("IV", "IIII").replace("IX", "VIIII")
        # s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        # s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        # res = 0
        # for v in s:
        #     res += r2i[v]
        # return res
        res = now = old = 0
        for v in reversed(s):
            old, now = now, r2i[v]
            if now < old:
                res -= now
            else:
                res += now
        return res


# @lc code=end

