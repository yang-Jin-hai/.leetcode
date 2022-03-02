#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
from functools import lru_cache


class Solution:
    def myPow(self, x: float, n: int) -> float:
        @lru_cache(None)
        def pow(n):
            if n == 0: return 1
            if n & 1:
                return x * pow(n-1)
            half = n >> 1
            return pow(half) * pow(half)
        return pow(n) if n > 0 else 1 / pow(-n)
# @lc code=end

