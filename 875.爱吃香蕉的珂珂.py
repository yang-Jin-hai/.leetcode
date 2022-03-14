#
# @lc app=leetcode.cn id=875 lang=python3
#
# [875] 爱吃香蕉的珂珂
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            m = (l+r)>>1
            v = 0
            for num in piles:
                v += (num - 1) // m + 1
            if v <= h:
                r = m
            else:
                l = m + 1
        return l
        # (1)
        # def getTime(m):
        #     t = 0
        #     for num in piles:
        #         t += (num-1) // m + 1
        #     return t
        # l, r = 1, max(piles)
        # while l <= r:
        #     m = (l+r)>>1
        #     if getTime(m) <= h:
        #         if m == 1 or getTime(m-1) > h:
        #             return m
        #         r = m - 1
        #     else:
        #         l = m + 1
    
# @lc code=end

