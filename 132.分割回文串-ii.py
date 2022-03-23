#
# @lc app=leetcode.cn id=132 lang=python3
#
# [132] 分割回文串 II
#

# @lc code=start
class Solution:
    def minCut(self, s: str) -> int:
        m = len(s)
        dp = [0] * m
        valid = [[False for i in range(m)] for i in range(m)]
        for i in range(m):
            for j in range(i+1):
                if s[i] == s[j] and (j+1 >= i or valid[j+1][i-1]):
                    valid[j][i] = True
        def isValid(l, r):
            return valid[l][r]
        for i in range(m):
            if isValid(0, i):
                dp[i] = 0
            else:
                dp[i] = i
                for j in range(1, i+1):
                    if isValid(j, i):
                        dp[i] = min(dp[i], dp[j-1]+1)
        return dp[-1]
# @lc code=end

