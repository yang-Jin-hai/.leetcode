#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#

# @lc code=start
from functools import lru_cache


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        for i in range(n + 1):
            if i <= 1:
                res[i] = i
            else:
                if i & 1:
                    res[i] = res[i>>1] + 1
                else:
                    res[i] = res[i>>1]
        return res
        # @lru_cache(None)
        # def count(n):
        #     if n <= 1:
        #         return n
        #     if n & 1:
        #         return count(n>>1) + 1
        #     return count(n>>1)
        # res = []
        # for i in range(n+1):
        #     res.append(count(i))
        # return res
# @lc code=end

