#
# @lc app=leetcode.cn id=564 lang=python3
#
# [564] 寻找最近的回文数
#

# @lc code=start
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        m = len(n)
        if m == 1: return str(int(n)-1)
        candidates = [10**(m - 1) - 1, 10**m + 1]
        def construct(x):
            y = x // 10 if m & 1 else x
            while x:
                y *= 10
                y += x % 10
                x //= 10
            return y
        init = int(n[:(m+1)>>1])
        num = int(n)
        for prefix in range(init-1, init+2):
            candidates.append(construct(prefix))
        diffs = [abs(num-v) for v in candidates]
        min_diff = 10 ** 18
        for i, diff in enumerate(diffs):
            if diff != 0 and diff < min_diff:
                min_diff, res = diff, candidates[i]
        return str(res)
                
        
# @lc code=end

