#
# @lc app=leetcode.cn id=115 lang=python3
#
# [115] 不同的子序列
#

# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n: return 0
        dp = [[0 for i in range(n+1)] for i in range(2)]
        for i in range(2): dp[i][0] = 1
        for i in range(m):
            for j in range(min(i+1,n)):
                if s[i] == t[j]:
                    dp[(i+1)%2][j+1] = dp[i%2][j] + dp[i%2][j+1]  
                else:
                    dp[(i+1)%2][j+1] = dp[i%2][j+1]
        return dp[m%2][-1]
# @lc code=end

