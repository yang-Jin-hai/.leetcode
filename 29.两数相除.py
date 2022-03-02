#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        ans = 0
        sign = 0
        if dividend < 0:
            dividend = -dividend
            sign = 1 - sign
        if divisor < 0:
            divisor = -divisor
            sign = 1-sign
        def posdivide(a, b):
            r = 0
            while a >= b:
                v, q = b, 1
                while a >= v + v:
                    v += v
                    q += q
                r += q
                a -= v
            return r
        ans = posdivide(dividend, divisor)
        if sign:
            return -ans
        return ans
# @lc code=end

